__author__ = 'qa185001'
from flask import Flask
from flask import jsonify, request, abort

app = Flask(__name__)

isPreprodDown = False


