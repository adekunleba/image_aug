from distutils.log import error
import io, os
import requests
from flask import Flask, request, render_template
from PIL import Image
import logging

# Imports for prediction
from app.image_augmentations import random_augmentation

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = int(os.environ.get('SEND_FILE_MAX_AGE_DEFAULT', 0))
# 4MB Max image size limit
app.config['MAX_CONTENT_LENGTH'] =  int(os.environ.get('MAX_CONTENT_LENGTH', 4 * 1024 * 1024))

# Default route just shows simple text
@app.route('/', methods=['GET'])
def index():

    try:
        image_url = request.args.get('url', None)
        if not image_url:
            return render_template("no_image.html")
    
        logging.info(image_url)
        quick_check = requests.head(image_url)
        
        if quick_check.status_code != 200:
            return render_template("error.html", error=ImageUrlNotReachable("Image url is not reachable")), quick_check.status_code

        # Can we have a size that overflow max int?
        cl = quick_check.headers.get('content-length', None)

        if cl != None:
            cl = int(cl)
            max_lenght = int(app.config.get('MAX_CONTENT_LENGTH', 4 * 1024 * 1024))
            if cl > max_lenght:
                logging.warn(f"Image file is too large")
                return render_template("error.html", error=ImageSizeLarge(f"ImageFileSize: Image size should be less than {max_lenght / (1024 * 1024)}MB")), 400

        image_response = requests.get(image_url, timeout=60)

        if image_response.status_code != 200:
            return render_template("error.html", error=ImageUrlNotReachable("Image url is not reachable")), quick_check.status_code
        
        image = Image.open(io.BytesIO(image_response.content))
        flipped_image, function_name = random_augmentation(image)
        flipped_image.convert('RGB').save(os.path.join(os.getcwd(), "app/static/augmented_image.jpg"))
        return render_template("index.html", aug_name=function_name)
    
    except Exception as err:
        logging.warn("There was an error: ", err)
        return render_template("error.html", error=err), 400


class ImageSizeLarge(Exception):
    
    def __init__(self, message: str) -> None:
        super().__init__(message)

class ImageUrlNotReachable(Exception):
    
    def __init__(self, message: str) -> None:
        super().__init__(message)


if __name__ == '__main__':
    # Run the server
    app.run(host='0.0.0.0', port=8000, debug=True)