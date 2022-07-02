import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask("__name__", static_folder=os.path.abspath("app/view/static/"),
                        template_folder=os.path.abspath("app/view/templates/"))

from app.controller import home_controller, contas_controller