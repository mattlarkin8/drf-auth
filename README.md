# **LAB - Class 33**

## **Project: Authentication and Production Server**

### Author: Matthew Larkin

### Setup

Ensure you have properly setup your `venv`. Install dependencies from `requirements.txt`.  

Use `python manage.py runserver` to test the site deployment on your local machine.  

If you have docker, use `docker-compose up --build` to build and test a Docker deployment of the Django app.

### Tests

Use ThunderClient or another HTTP client to test the API routes.  

You should be able to:

- Hit the default route `http://localhost:8000/` and get the Snack List view. (Requires authentication token)
- Go to the Snack Detail view for any snack using its id. Ex: `http://localhost:8000/1/` (Requires authentication token)
- Obtain your token pair by going to `http://localhost:8000/api/token/`
- Refresh your access token by going to `http://localhost:8000/api/token/refresh`
