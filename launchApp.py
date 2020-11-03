from flask import Flask, render_template
from apis import api

from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api.init_app(app)

app.run(debug=True)