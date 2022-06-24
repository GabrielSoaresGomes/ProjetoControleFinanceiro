import os
from flask import Flask


app = Flask("__name__", static_folder=os.path.abspath("app/view/static/"),
                        template_folder=os.path.abspath("app/view/templates/"))

from app.controller import home_controller