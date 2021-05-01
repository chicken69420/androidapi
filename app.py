from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse
import json
from flask_autoindex import AutoIndex
import werkzeug


app = Flask(__name__)
api = Api(app)
app.run()
