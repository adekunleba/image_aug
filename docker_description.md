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

Update to v.0.0.3
### Running with dynamic variable mappings.
- Allows you to set the following as environment variables.
a. PORT - Running port  of the app, but will still map to 8000 on server.
b. MAX_CONTENT_LENGTH - Maximum image size allowed
c. SEND_FILE_MAX_AGE_DEFAULT - Cache age of images.

Ensure you set this values by `export KEY:VALUE` from command line else at most the port mapping will not work hence the compose itself won't build

Updated Docker compose will look like this.

```
version: "3"
services:
  app:
    image: tonytunde2012/image_aug:latest
    ports:
      - "8000:${PORT}"
    environment:
      - PORT=${PORT}
      - MAX_CONTENT_LENGTH=${MAX_CONTENT_LENGTH}
      - SEND_FILE_MAX_AGE_DEFAULT=${SEND_FILE_MAX_AGE_DEFAULT}
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

And if running with normal docker run can do.

```
docker pull tonytunde2012/image_aug:latest

docker run -p 8000:8000 -e KEY=VALUE tonytunde2012/image_aug

```

_PS: The project has been built with the defualt allowable with v.0.0.2, Hence can decide not to use the updated compose_