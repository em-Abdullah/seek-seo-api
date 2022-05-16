from flask import Flask, make_response, render_template
from analyzer import analyze
from flask import request
from flask import url_for
from bs4 import BeautifulSoup
from operator import itemgetter


app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        args = request.args
        content = args.get('url')
    output = make_response(analyze(
        content, follow_links=False, analyze_headings=True, analyze_extra_tags=True))
    output.headers['Access-Control-Allow-Origin'] = '*'
    return output
