from flask import Flask, make_response, render_template
from seoanalyzer import analyze
from flask import request
from flask import url_for


app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        args = request.args
        content = args.get('url')
    output = make_response(analyze(content, follow_links=False))
    output.headers['Access-Control-Allow-Origin'] = '*'
    return output
