from flask import Flask, send_file
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)
app.run()
