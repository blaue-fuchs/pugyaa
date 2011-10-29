# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
app = Blueprint("root", __name__)


@app.route("/")
def root():
    return render_template("index.html")
