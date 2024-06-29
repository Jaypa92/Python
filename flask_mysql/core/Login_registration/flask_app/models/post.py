from flask_app import Flask
from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)