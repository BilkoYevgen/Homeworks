from flask import Flask
from logging.config import dictConfig
from .config import AppConfig


app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] - %(levelname)s:  %(message)s',
    }},
})

app.config.from_object(AppConfig)

from .views import *