from . import main
from flask import render_template,request,url_for,flash
from .. import db


@main.route('/')
def login():
  
  return "<h1> ******you are a main login and testing braching ,MARTIN you can merge the Branch  *****</h1>"