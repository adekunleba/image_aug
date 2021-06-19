#### Image augmentation 

**Established goal** - Have a web application that serves image augmentation.
Also, should have the capability to do Continous Integration/Development.
Should run in a docker environment

**Consideration**:
Flask deployment should be at least with gunicorn allows production-case deployment and configuration for the flask app.

**Tasks**:
- Develop a bare minimum of the current running application.
- Provide a Dockerfile for this
- Do more data augmentation and test
- Create a repo for the project
- Create a github action flow for test and production (considering that we are likely to be using the other-branch-main approach to commits) 
- Deploy our first example to dockerhub
- Add another data augmentation and test

**Time of project**
App code and deployment of working copy -  approximately 2 hours 30min
Most minutes spent on github actions.

**Other Improvement Tasks**:
- Handle error in web app effectively
  Edge cases:
    - If no image passed to url
    - If an error occured while doing augmentation
    - Image that are too big to view, just resize it to say 700 * 700
    - Image whose size is above 4MB

      To manage this, we can request only the header of the image url at first and then check the content lenght (if provided) before we go ahead and load the image into memory. If its size is greater than our max content lenght, just tell user to look for some smaller image to check.
    - Request to an image is taking long or not found
- Give name to image augmentation shown
- Do code scanning to ensure there is no vulnerabilities and password exposure
- Use `.snyk` to ensure that libraries being used are also not vulnerable to attack.
- Auto include docker description in the project once your deploy. Allows us to have a **Docker hub readme** that can be updated easily once the docker deployment is done.

**Observed constraints**:
- Project is minimal, what scale should we make it. My answer, enough to ensure that we can deploy a sample of such to a production server
- Providing unittest for image augmentation is tricky as to test you might need some extensive algorithms to evaluate if an augmentation actually happened else doing just image height checks to ensure the image is returned properly.
- Also, images are being overwritten for every new request to api, probably consider saving to filesystem instead and retrieving its url, this allows to keep all images and its augmentation.
- There is no constraint on how to approach the Github action deployment.

**Challenges**:
My aim is to keep the docker image as small as possible, hence I used the alpine python docker image as my base, however,some python libraries need some other native dev libraries e.g bcrypt, I had to add these developer tools to the linux docker build hence increasing the size of the docker. This is somewhat a necessary evil.


#### Deployment

The project is deployed to this [docker hub link](https://hub.docker.com/r/tonytunde2012/image_aug)

**Running the model using docker-hub image**

Can use either of the approaches to run the project:

**A. Using a docker compose with watch_tower for continous deployment**:
```
version: "3"
services:
  app:
    image: tonytunde2012/image_aug:latest
    ports:
      - "8000:8000"
    restart: always
  
  watchtower:
    image: containrrr/watchtower:latest
    container_name: watchtower
    environment:
      WATCHTOWER_CLEANUP: 'true'
      WATCHTOWER_REMOVE_VOLUMES: 'true'
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always
```

**B. Using basic docker run**:
This will require manual redeployment everytime the image changes
```
docker pull tonytunde2012/image_aug:latest

docker run -p 8000:8000 tonytunde2012/image_aug

```

**Running the application**
The application runs on port 8000 in your deployment server.

Retrieving an image augmentation is by making a request like this:
http://0.0.0.0:8000/?url=<image_url>

for example:
http://0.0.0.0:8000/?url=https://imgs.xkcd.com/comics/bad_code.png
