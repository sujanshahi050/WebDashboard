# File that contains routes for the web app
from myapp import app


import json
import plotly.utils
from flask import render_template
from scripts.data import return_figures


@app.route('/')
@app.route('/index')
def index():

    figures = return_figures()
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    print(figuresJSON)
    return render_template('index.html', ids=ids, figuresJSON=figuresJSON)