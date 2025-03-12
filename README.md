# Planetarium

The "Planetarium" project allows users to view astronomy shows, book tickets for sessions, and access information about sessions and shows. It also provides an API for managing astronomy shows and planetarium sessions.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Project Setup](#project-setup)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [Contributing](#contributing)

## Features

- Create and view astronomy shows
- Create and view planetarium sessions
- Upload images for shows
- Filter shows by actor and title
- User authentication
- Support for uploading and managing images for each show

## Technologies

The project uses the following technologies:

- **Python 3.8+**
- **Django 3.2+** for backend development
- **Django Rest Framework** for building the API
- **PostgreSQL** as the database
- **Docker** for containerization
- **Pillow** for image processing

## Project Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/oboliziuk/planetarium-booking/
   cd planetarium
   
2. Create the .env file: Create a .env file at the root of the project and add the following environment variables:
   ```bash
   POSTGRES_DB=your_database_name
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432

3. Start the Docker container: To start the project in Docker containers, run:
    ```
    docker-compose build
    docker-compose up 

This will build and start all necessary containers for your project.

4. Apply database migrations: After the containers are running, apply the migrations to create the database:
   ```
   docker-compose exec web python manage.py migrate   

5.Running the Project
Once everything is set up, open your browser and navigate to:
```
http://localhost:8000
```
This will let you access the project.
For interacting with the API, you can use the following endpoints:
```
/api/astronomyshows/ - List of astronomy shows
/api/showsessions/ - List of planetarium sessions
```