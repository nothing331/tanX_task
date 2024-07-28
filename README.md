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
3. Create a `.env` file with the necessary content (replace with your actual values)
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
