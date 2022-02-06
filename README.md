# 123&Me: An Interactive Platform for Numerical Literacy of Young Children

123&Me is a platform designed to help younger children learn to read and write numbers, as well as basic numeracy to test understanding. As such, it's benefits are threefold:
- Allows teaching for younger children to be fully autonomous, allowing for easy and accessible teaching, especially given high childcare costs
- Aids in the increasingly important need to move towards a paperless world
- Capitalises on the widespread access to touchscreen devices
- Allows educators to help children gain numerical literacy more quickly.

123&Me is designed to be simple and intuitive, especially for it's younger audience. With fewer, larger buttons and a large canvas on which children can draw, it is easy to understand and use, possibly required only a quick demo from a supervising adult.
There are five buttons:
- Clear: To clear your board
- Check: To check your answer
- Shuffle: To give you a new number to copy, to be used initially by kids
- Add: Provides basic addition
- Subtract: Provides basic subtraction

The frontend is written in JavaScript, HTML and CSS.

The backend is written in Python-Django, with numerical analysis being computed by a CNN machine learning model we trained using the MNIST dataset.

## Prerequisites

This project requires Python to be installed on your computer. Python can be installed by following the instructions written on the web page below:

https://devpost.com/software/427641/joins/Ru6PWgnrWdJYyBJGMXUYIQ

Note: this project was tested on Python version 

This project also requires the presence of various pip packages, which can be installed by running the following command in the home directory:

```
$ pip install -r requirements.txt
```
Lastly, we also need a web server that hosts the `frontend` directory of this project. An example of such a server is the ![Web Server for Chrome](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb), which a Chrome extension.
Note: the frontend must be hosted on the URL `http://127.0.0.1:8887`

## Getting Started
To start the Django server, navigate inside the `backend` direectory and execute the following command:
```
$ python3 manage.py runserver 8000
```
This will start a backend server at URL `http://127.0.0.1:8000`.
After starting the backend server, start the server hosting the frontend. Then visit the URL `http://127.0.0.1:8887` to start the application.

## Screenshots


## Creators
This project was made by Rishav Chatterjee, Krish Maha, Dhruv Jimulia, Aaryan Dharmadhikari and Ankit Sh