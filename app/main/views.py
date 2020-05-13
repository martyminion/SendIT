from . import main
from flask import render_template,request,url_for,flash
from .. import db
from ..tokengenerator import autogenerate_token


@main.route('/')
def index():
  
  return render_template('index.html')