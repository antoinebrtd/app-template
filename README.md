## Requirements

* Docker and Docker-compose
* Python 3
* Node 10 and NPM

## Getting started

* In the root folder, start the containers with `docker-compose up -d`
* In the `back` folder, create a virtual environment and install the requirements (`pip install -r requirements.txt`)
    * To launch the web server : `python run.py`
    * To launch the scheduler : `python clock.py`
    * To launch the worker : `rq worker -c template.core.cache`
* In the `front` folder, just run `npm install` to install the dependencies
    * To launch the front : `npm run dev`
    * To build the front (to deploy) : `npm run build`