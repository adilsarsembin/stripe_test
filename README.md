# Stripe sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/adilsarsembin/stripe_test
$ cd stripe_test
```
Make sure that Python is installed on your machine.

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ venv/Scripts/activate.bat
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Make sure your database was initialized in .env file. Here is the look to .env file: <br />
SECRET_KEY=<br />
NAME=<br />
USER=<br />
PASSWORD=<br />
HOST=<br />
PORT=<br />
STRIPE_KEY=<br />

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/gocardless/`.
