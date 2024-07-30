# Cryptocurrency Price Alert Application

This application allows users to set price alerts for cryptocurrencies and receive email notifications when the target price is reached.
This repository is the submission of TanX.fi Online assignment, it's function is to set price alerts for cryptocurrencies and receive email notifications when the target price is reached

## Features

- User registration and authentication using JWT tokens
- Create, delete, and fetch price alerts
- Real-time price updates using Binance WebSocket
- Email notifications when price alerts are triggered
- Caching layer for fetching alerts
- Pagination and filtering options for fetching alerts

## Technologies Used

- Backend: Flask (Python)
- Database: PostgreSQL
- Real-time Updates: Binance WebSocket
- Email: SMTP (Gmail)
- Containerization: Docker and Docker Compose

## Setup and Running

1. Clone the repository
2. Make sure you have Docker and Docker Compose installed
3. Create a `.env` file with the necessary content (replace with your actual values), put you email and smpt password there
4. Run the following command to start the application:

```
docker-compose up --build

docker-compose up -d
```

## API Endpoints

### Authentication

- `POST /register`: Register a new user
# formate 
'''
{
	  "username": "ayush", 
    "email":"ayush33156@gmail.com",
    "password": "123"
}
'''
- `POST /login`: Login and receive a JWT token
# formate 
'''
{
	  "username": "ayush", 
    "password": "123"
}
'''

### Alerts
- For the alerts it is recommended to only use '''BTCUSDT''' or '''ETHUSDT'''
- `POST /alerts/create`: Create a new alert (JWT required)
- `DELETE /alerts/delete/<alert_id>`: Delete an alert (JWT required)
- `GET /alerts/`: Fetch all alerts for the authenticated user (JWT required)
  - Query parameters:
    - `page`: Page number (default: 1)
    - `per_page`: Number of items per page (default: 10)
    - `status`: Filter alerts by status

## The Proccess of running and buildeing docker 

Here I will be explaining my docker-compose.yml file

'''
web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - postgres
      - redis
    networks:
      - theworld
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://user:password@postgres:5432/alertsdb
'''

This code defines our webservies
'''build: .''' tells us to create the image in current directory

'''ports: - "5000:5000"''' maps port 5000 to port 5000 of the container

'''depends_on''' - ensure that postges and redis servers are working

'''networks''' - connects this server to the world network to make connection with all other images like postgress and redis
'''environment''' - sets the environment

'''
postgres:
    image: postgres:13
    hostname: postgres
    networks:
      - theworld
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=alertsdb
    volumes:
      - ./migrations:/app/migrations
      - postgres_data:/var/lib/postgresql/data
'''
This defines your PostgreSQL service:

- It uses the official postgres:13 image.
- Sets the hostname to "postgres" database.
- Connects to the "theworld" network.
- Sets environment variables for the database 
- name, user, and password.
- Mounts two volumes: one for migrations which will enable us to create tables in postgresql
- one for persistent data storage.

'''
volumes:
  postgres_data:
  migrations:
'''

This section defines named volumes used by the services.


'''
networks:
  theworld:
    driver: bridge
'''

This creates a custom bridge network named "theworld" that all services can use to communicate with each other.

# Project Structure:
'''
/project
    /app
        __init__.py
        /models
          alert.py
          user.py
        /routes
          alerts.yp
          auth.py
        /servies
          email_service.py
          price_service.py
    /migrations
    /task
    extensions.py
    config.py
    Dockerfile
    docker-compose.yml
    Dockerfile
    README.md
    requirements.txt
    run.py
    wsgi.py
'''

__init__.py 
- Contains link to all the rounts, extentions, webstocket call and other service code
- Initializes the Flask application

model folder 
- contain schema for our user and alerts table which store data of user and there alert info in the database

routes folder 
- Has routes to implement JWT tokena and get creat dealeat and see all alerts
- alerts : has routes to cleate/delete and see all the alerts and there status

services folder
- preice_service : his folder fetches the information from the websocket for BTCUSDT and ETHUSDT currenct and uses the logic to compare with the user target amount and the call email_services.py
- email_services.p :  used to send mail

extensions.py
- used to setup and calling the database, JWT and redis

config.py 
-contains important dat we need throw out the project