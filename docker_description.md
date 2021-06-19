Repository for docker hub

##### Description
Image is a simple flask application that allows you to view your data augmentations

##### Docker environment specification.
Uses `python 3.9.4` and `AMD` environment.

Project itself was tested with python `3.8` and `3.9` environment.


#### Running the docker
Running the docker can be in two different approaches.

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