Image augmentation 

Established goal - Have a web application that serves image augmentation.
Also, should have the capability to do Continous Integration/Development.
Should run in a docker environment

Observed constraints:
Project is minimal, what scale should we make it.
Providing unittest for image augmentation is tricky as to test you might need some extensive algorithms to evaluate if an augmentation actually happened else doing just image height checks to ensure the image is returned properly.
Not sure if there is a need to be able to serve more than one image
Also, images are being overwritten for every new request to api.
There is no constraint on how to approach the Github action deployment.

Consideration:
Flask deployment should be at least with gunicorn allows production-case deployment and configuration for the flask app.

Tasks:
- Develop a bare minimum of the current running application.
- Provide a Dockerfile for this
- Do more data augmentation and test
- Create a repo for the project
- Create a github action flow for test and production (considering that we are likely to be using the other-branch-main approach to commits) 
- Deploy our first example to dockerhub
- Add another data augmentation and test


Challenging part of the project:
Basically highlighting some challenges faced during working on the task.
As my aim is to keep the docker image as small as possible, hence I used the alpine python docker image as my base, however, following the requirements of some .so for various python packages e.g bcrypt, I had to add some developer tools to the linux environment hence increasing the size of the docker. This is somewhat a necessary evil.
