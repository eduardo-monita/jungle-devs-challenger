# jungle-devs-challenger
The purpose of this challenge is to give an overall understanding of a backend application. You’ll be implementing a simplified version of a news provider API.

## Requirement
If you want to run the project, first make sure you have the docker installed on your computer. If not, you can get it by clicking [here](https://docs.docker.com/get-docker/ "here").

Soon after, clone this repository to your computer and enter the project root folder:

      git clone https://github.com/eduardo-monita/jungle-devs-challenger.git
      cd jungle-devs-challenger
        
## Run project 
Once you are at the root of the project you need to run the following commands to run the project:

### Development
Docker Compose to Development
- `docker-compose build` (build your containers). Note: Only needed for the first time running the project.
- `docker-compose up -d` (start runing containers). Note: The first time you run the command it will start creating the database, so it may take a little longer than usual.
- Note: To remove containers, follow the following command: `docker-compose down` (remove up containers)
#### Container configuration
To configure the container you will need to access it, so pay attention to which environment you are in (will show something like this on your terminal `root@b81a9b80611a:/app#`).
- `docker exec -it jungle-devs-challenger-web-dev bash` (Access web container)
- `python manage.py migrate` (Generate all database tables)
- `python manage.py collectstatic --no-input` (Download all static files)
- `python manage.py createsuperuser` (creates a user to access in /admin and in other API)
- Finnaly the project is running, so open this link in your browser: [http://localhost:8080/](http://localhost:8080/ "http://localhost:8080/")
   
### Production
Docker Compose to Production
- `docker-compose -f docker-compose.prd.yml build` (build your containers). Note: Only needed for the first time running the project.
- `docker-compose -f docker-compose.prd.yml up -d` (start runing containers). Note: The first time you run the command it will start creating the database, so it may take a little longer than usual.
- Note: To remove containers, follow the following command: `docker-compose -f docker-compose.prd.yml down` (remove up containers)
#### Container configuration
To configure the container you will need to access it, so pay attention to which environment you are in (will show something like this on your terminal `root@b81a9b80611a:/app#`).
- `docker exec -it jungle-devs-challenger-web-prd bash` (Access web container)
- `python manage.py migrate` (Generate all database tables)
- `python manage.py collectstatic --no-input` (Download all static files)
- `python manage.py createsuperuser` (creates a user to access in /admin and in other API)
- Finnaly the project is running, so open this link in your browser: [http://localhost:9100/](http://localhost:9100/ "http://localhost:9100/")
        
## Endpoints
For more information about endpoints, you can go to `/ swwagger /` or `/ redoc /`. Note: base url from swagger is `/api/`.
Endpoints |HTTP | Results
-- | -- |-- 
`/api/login/` | POST | Check the credentials and return the REST Token
`/api/sign-up/` | GET,POST | Calls Django logout method and delete the Token object assigned to the current User object
`/api/password/change/` | POST | Calls Django Auth SetPasswordForm save method
`/api/user/` | GET,PUT,PACTH | Reads and update django user
`/api/admin/authors/` | GET,POST | List and Create authors
`/api/admin/authors/:id` | GET,PUT,PATCH,DELETE | Reads, update and delete author
`/api/admin/articles/` | GET,POST | List and Create articles
`/api/admin/articles/:id` | GET,PUT,PATCH,DELETE | Reads, update and delete articles
`/api/articles/?category=:slug` | GET | List all articles
`/api/articles/:id/` | GET | Article Detail
`/admin/` | GET | To access Django's default administrator
`/swwagger/` | GET | API documantation
`/redoc/` | GET | API documantation

## Unit test
- To run the unit test, follow the command below:

        python manage.py test
        
## Image optimization
This project use library `autocrop` from pypi to perform face detection crop to field picture in author, you can read more about this library cliking [here](https://github.com/leblancfg/autocrop "here").
