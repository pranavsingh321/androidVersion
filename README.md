

## Endpoints
For the task we want you to create the following endpoints for the REST API:

* Endpoint 1 - POST apk
```
Description: Upload apk
URL: POST /api/applications
```

* Endpoint 2 GET all APKs
```
Description: Get all uploaded APKs
URL: GET /api/applications
```

* Endpoint 3 APK details
```
Description: Get apk details
URL: GET, PUT, DELETE /api/applications<id>
```


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
gunicorn --bind 0.0.0.0:8000 apkInfo.wsgi&
```
## Test
```
Preferably use any Rest Client like Postman(Chrome), RestClient(Mozilla) to open http://127.0.0.1:8000/scans.

```


