#  Project: Coffe Shop Website Fronted and Backend
A scalable coffee shop website with service management, a blog with categories, a contact form, and a custom Django 
administrator panel.

## Prerequisites:
You must have the following tools installed globally on your machine:

- Docker
- PostgreSQL (Recommended)

## Installation:

Clone the repo via git:
```sh
git clone git@github.com:Jescad29/webempresa.git
```

## Initial project setup:

Add the following environment variables to the env file, it is recommended to use `https://mailtrap.io/home for testing.`

```sh
	EMAIL_H = ' '
	EMAIL_HOST_U = ' '
	EMAIL_HOST_P = ' '
	EMAIL_P = ' '

```

## Running the aplication:
Server: `127.0.0.1:8000/`

To run the application, execute the following commands in this order.

- Run docker-compose up, and Compose starts and runs the entire application.
 ```sh
docker-compose up
```

## Create the first migration:

- Run docker-compose up -d to run Docker Compose in the background.
```sh
docker-compose up -d
```
- Run docker-compose exec django sh to enter the django terminal
```sh
docker-compose exec django sh
```


