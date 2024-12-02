from flask import Flask,Blueprint,render_template

bp=Blueprint("index",__name__)

@bp.route('/')
def home():
    return "homepage"