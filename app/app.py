import io, os
import requests
from flask import Flask, request, render_template
from PIL import Image
import logging

# Imports for prediction
from app.image_augmentations import random_augmentation

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# 4MB Max image size limit
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024 

# Default route just shows simple text
@app.route('/', methods=['GET'])
def index():
    image_url = request.args.get('url')
    logging.info(image_url)
    image_response = requests.get(image_url)
    image = Image.open(io.BytesIO(image_response.content))
    flipped_image = random_augmentation(image)
    flipped_image.convert('RGB').save(os.path.join(os.getcwd(), "app/static/augmented_image.jpg"))
    return render_template("index.html")

