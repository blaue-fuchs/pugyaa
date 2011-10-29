# -*- coding: utf-8 -*-
import os
from flask import Flask
from views import root, register

app = Flask(__name__)
app.register_blueprint(root.app, url_prefix="/")
app.register_blueprint(register.app, url_prefix="/register")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5008))
    app.run(host='127.0.0.1', port=port, debug=True)
