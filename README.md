# Amazon-Price-Tracker
A exam project for "Programmieren in Python". It shows the prices and its development of a specific product.

## Setup

You need to setup a virtual enviroment for the developing with Python and Django.

- [Virtual enviroment](https://docs.python.org/3/tutorial/venv.html)
- [Install Django](https://docs.djangoproject.com/en/5.1/topics/install/)

## Running the Django Server

Please refer to the docs for more information about running the Django server [`here`](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)

To start the server, go the "Amazon-Price-Tracker" folder, open a terminal and type:
```bash
  python manage.py runserver
```
... into the command line.

You should see something like this: 

> December 10, 2024 - 19:27:22
> Django version 5.1.4, using settings 'amazon_price_Tracker.settings'
> Starting development server at http://127.0.0.1:8000/
> Quit the server with CONTROL-C. 

Watch this [video](https://www.youtube.com/watch?v=nGIg40xs9e4) for a brief introduction into Django!

## Tasks for Everyone

- frontend UI development (Matthis)
  - display some charts (matplotlib) (Thomas)
- API endpoints for fetching data from an Amazon API (Simon)
- convert / work with the incoming data -> filter out important data to us (Jannis, Max)
- store data (?)
