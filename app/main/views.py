from . import main
from flask import render_template,request,url_for,flash
from .. import db


@main.route('/')
def index():
  
  return render_template('index.html')