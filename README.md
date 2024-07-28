# Cryptocurrency Price Alert Application

This application allows users to set price alerts for cryptocurrencies and receive email notifications when the target price is reached.

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
- Caching and Message Broker: Redis
- Real-time Updates: Binance WebSocket
- Email: SMTP (Gmail)
- Containerization: Docker and Docker Compose

## Setup and Running

1. Clone the repository
2. Make sure you have Docker and Docker Compose installed
3. Create a `.env` file with the following content (replace with your actual values):

4. Run the following command to start the application:
   docker-compose up --build
   docker-compose exec web flask <command>
   docker-compose exec db psql -U user -d alertsdb
   docker-compose exec redis redis-cli
   docker-compose logs web
   docker-compose up -d --no-deps --build web
   docker-compose exec web flask db init
  docker-compose exec web flask db migrate -m "Initial migration"
  docker-compose exec web flask db upgrade

   
5. The application will be available at `http://localhost:5000`

## API Endpoints

### Authentication

- `POST /register`: Register a new user
- `POST /login`: Login and receive a JWT token

### Alerts

- `POST /alerts/create/`: Create a new alert (JWT required)
- `DELETE /alerts/delete/<alert_id>`: Delete an alert (JWT required)
- `GET /alerts/`: Fetch all alerts for the authenticated user (JWT required)
- Query parameters:
 - `page`: Page number (default: 1)
 - `per_page`: Number of items per page (default: 10)
 - `status`: Filter alerts by status

## Solution Details

1. The application uses Flask as the web framework and SQLAlchemy as the ORM for database operations.
2. User authentication is implemented using Flask-JWT-Extended.
3. Real-time price updates are obtained using Binance WebSocket client.
4. When a price alert is triggered, an email is sent to the user using SMTP (Gmail).
5. Redis is used for caching the results of the "fetch all alerts" endpoint.
6. The application is containerized using Docker, and services are orchestrated using Docker Compose.

## Improvements and Considerations

- Implement proper error handling and logging
- Add input validation and sanitization
- Implement rate limiting to prevent abuse
- Use a dedicated email service like SendGrid for better deliverability
- Implement a more robust task queue system for sending emails (e.g., Celery with Redis as the broker)
- Add unit and integration tests
- Implement proper security measures for storing sensitive information (e.g., use environment variables or a secrets management system)
