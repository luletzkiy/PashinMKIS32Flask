from flask import Flask, render_template, request
import subprocess
import os
import jsonlines

app = Flask(__name__)

import os
dirname = os.path.dirname(__file__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/contacts/')
def contacts():
    developer_name = "Nick"
    context = {'name': developer_name}
    return render_template('contacts.html', props=context)

@app.route('/parser/')
def parser_get():
    return render_template('parser.html')

@app.route('/parser/', methods = ['POST'])
def parser_post():
    spider_name = "CatalogSpider"
    subprocess.check_output(f'scrapy crawl catalog -a pagesnum={request.form["pages"]} -o output.jsonl')
    filename = os.path.join(dirname, 'output.jsonl')
    data = []
    with jsonlines.open(filename) as reader:
        for obj in reader:
            data.append(obj)
    return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
