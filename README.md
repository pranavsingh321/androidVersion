

## Endpoints
For the task we want you to create the following endpoints for the REST API:

* Endpoint 1 - POST scan
```
Description: Create a new scan
URL: POST /scans
Request data: json data representing a scan (see above), i.e. {“points”: [<points>]}
Return: {“id”: <id>, “points”: [<points>]} where the id is created by the backend can be used later when asking for scans
```

* Endpoint 2 GET scan
```
Description: Get the points of a specific scan
URL: GET /scans/<id>
Return: {“id”: <id>, “points”: [<points>]}
```

* Endpoint 3 PUT scan
```
Description: Create or update a scan with a specific ID
URL: PUT /scans/<id>
Request data: A scan object {“id”: <id>, “points”: [<points>]}
Return: {“id”: <id>, “points”: [<points>]}
```

* Endpoint 4 - GET bounding box
```
Description: Get the bounding box of a scan (specified by the id from Endpoint 1) 
URL: GET /scans/<id>/boundingbox
Return: {“boundingBox”: [<x_l>, <y_l>, <z_l> ] , “center”: [<x>, <y>, <z>]}
```

## General notes 
- When implementing the task, there’s no need to use a database to store the scans, an in memory data structure is just fine



## Setup and start
```
It's a Django project based on Python 2.7.9 and assumes that execution environment already has Python and PIP installed. 

git  clone git@github.com:pranavsingh321/androidVersion.git
cd androidVersion
pip install virtualenv
virtualenv ENV
source ENV/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
cd apkInfo/
python manage.py migrate --run-syncdb
gunicorn --bind 0.0.0.0:8000 boundingbox.wsgi&
```
## Test
```
Preferably use any Rest Client like Postman(Chrome), RestClient(Mozilla) to open http://127.0.0.1:8000/scans.

or

open the browser at url - http://127.0.0.1:8000/scans

For sample tests using curl-

cd software-challenge-pranav
./test.sh
```


