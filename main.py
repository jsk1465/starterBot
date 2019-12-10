# import os
# import re
# from slackclient import SlackClient
from flask import Flask,request
import json


app = Flask(__name__)

@app.route('/query-example')
def query_example():
    # language = request.args.get('language') #if key doesn't exist, returns None
    # framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    # website = request.args.get('website')
    return json.dumps(request.args)
    # return '''<h1>The language value is: {}</h1>
    #           <h1>The framework value is: {}</h1>
    #           <h1>The website value is: {}'''.format(language, framework, website)

@app.route('/')
def hello():
    s = "Not JSON"
    if(request.is_json):
        s = request.get_json()
    return s

if __name__ == "__main__":
    app.run(debug=True)