from flask import Flask
from flask import render_template
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/html/')
def html():
    json_data = None
    with open('templates/html.json', 'r') as f:
        json_data = json.load(f)
    return jsonify(json_data);

@app.route('/css/')
def css():
    json_data = None
    with open('templates/css.json', 'r') as f:
        json_data = json.load(f)
    return jsonify(json_data)

@app.route('/js/')
def js():
    json_data = None
    with open('templates/js.json', 'r') as f:
        json_data = json.load(f)
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

