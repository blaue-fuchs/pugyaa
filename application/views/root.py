# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
app = Blueprint(__name__, "root")


@app.route("/")
def index():
    return render_template("index.html")
