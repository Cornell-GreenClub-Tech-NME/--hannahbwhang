# Intro To Backend Development

## Setup

Create a virtual environment and install the requirements located in src/requirements.txt. Here are the commands if you haven't done this before.
```
$ python -m venv venv
``` 
This line creates a virtual environment. Depending on your version, you may need to replace ```python``` with ```python3```.
```
$ source ./venv/bin/activate
```
This is how you activate the virtual environment. Now that you have it activated, we can install the requirements.
```
$ pip install -r requirements.txt
```
Next, let's do some setup to make sure our app runs properly.
```
$ python manage.py migrate
```

Finally, try running the app using ```python manage.py runserver```.
You should be able to go to localhost:8000 using a web browser or Postman and see some output there. To stop the app from running, you can use ```CTRL+C```.

## TODO

Your task is to create a model for Transactions, as well as 2 new routes for the API. Please complete those following the specifications, which can be found at ``` ./api_spec.md```.

