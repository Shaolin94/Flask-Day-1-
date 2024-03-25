from flask import Flask

app = Flask(__name__)

# import the route to the application
from . import routes