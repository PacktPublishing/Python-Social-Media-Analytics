"""
2. Distributed Computing : Celery
"""

"""

# Getting Started Tutorial
http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

# Installing Celery
pip install celery

# Install Message Broker : RabbitMQ
Celery requires a solution to send and receive messages; 
usually this comes in the form of a separate service called a message broker.

# Default Backend Broker : rpc temporary messaging service
For better performance use RabbitMQ or Redis

## RabbitMQ Install Linux example

Tutorial for installing rabbitmq 
https://www.rabbitmq.com/download.html

Installing
sudo apt-get install rabbitmq-server

That should automatically start the server if not do the following:
sudo service rabbitmq-server start

To stop the service
sudo service rabbitmq-server stop


## Celery Setup
mkdir celery_tasks
$create file tasks$

## Celery Start Worker
cd celery_tasks
celery -A tasks worker --loglevel=info

## Using Celery 
cd celery_tasks
create file run_tasks
python run_tasks.py

"""

"""
# Running Celery Using Docker

Building the image
docker build -t test/celery .



"""
