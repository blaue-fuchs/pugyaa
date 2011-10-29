# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, make_response, request, redirect, url_for
app = Blueprint("register", __name__)
try:
    from application.utils.register import make_authorize_url, get_access_token, save_access_token
except:
    from utils.register import make_authorize_url, get_access_token, save_access_token


@app.route("/")
def index():
    url, secret = make_authorize_url()
    response = make_response(render_template("register.html", url=url))
    response.set_cookie('oauth_token_secret', secret)
    return response


@app.route("/set/")
def set():
    token = request.args.get("oauth_token", "")
    secret = request.cookies.get("oauth_token_secret", "")
    access_token = get_access_token(token, secret)
    is_finish = save_access_token(access_token)
    return redirect(url_for("/"))
