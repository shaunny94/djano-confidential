# DATHENA ASSIGNMENT

This assignment consists of a backend which is written using a DJANGO REST API FRAMEWORK and a frontend which is written in React JS. The backend exposes endpoint urls eg: http://localhost:8000 which is to be consumed by the front end which then renders the data onto the browser

The backend scripts are in the api folder whereas the front end scripts are in the frontend folder.The directory structure is as shown below

##Backend Folder Structure
```
    api
    | 
    |__api 
    |   | 
    |   |__settings.py 
    |   | 
    |   |__urls.py
    |   | 
    |   |__wsgi.py 
    |__fixtures 
    |   | 
    |   |__jsonfiles provided by Dathena
    |__mock_data 
    |   | 
    |   |__admin.py 
    |   | 
    |   |__models.py  #this is where the database tables are created
    |   | 
    |   |__serializers.py
    |    |
    |    |__urls.py #url of the endpoints
    |    |
    |    |__views.py
    |
    |___db.sqlite3 #database is created here
    |
    |___Dockerfile
    |
    |___manage.py #this is where commands are run to create a localhost
    |
    |__requirements.txt #install dependencies for the docker image 
```


## Instructions for Backend(Exposing the end point urls)

Step 1:
cd into the api folder

```bash
cd api
```
Step 2a:(Without Docker)
Run the Django localhost, this will run it on port 8000 by default

```bash
python manage.py runserver
```

Step 2b:(With Docker)
Build the image first, followed by running the docker container. These two processes can be run by the Dockerfile. The default port number would be 8000

```bash
docker build -t <reponame> eg: django/rest .
docker run <reponame>
```

Step 3:
Call the endpoints via your browser. There should be 6 endpoints for each json file 

```bash
http://localhost:8000/confidentialdata/
http://localhost:8000/confidentiallabels/
http://localhost:8000/doctypedata/
http://localhost:8000/doctypelabels/
http://localhost:8000/languagedata/
http://localhost:8000/languagelabels/

```

##Instructions for front-end

Step 1:
cd into the frontend folder

```bash
cd frontend
```

Step 2:
start the react project: first is to install the necessary dependencies followed by starting the server

```bash
npm install 
npm start
```
Step3:
Clicking on the options will render the json data provided by Dathena



Thanks for reading!! Feel free to contact me if you are unable to understand/view the scripts




