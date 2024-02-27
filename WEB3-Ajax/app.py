from flask import Flask
from flask import render_template
from flask import jsonify
import json

app = Flask(__name__)

def read_json(file_location):
    json_data = None
    with open(file_location, 'r') as f:
        json_data = json.load(f)
    return json_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list/')
def list():
    json_data = read_json('templates/list.json')
    return jsonify(json_data)

@app.route('/html/')
def html():
    json_data = read_json('templates/html.json')
    return jsonify(json_data)

@app.route('/css/')
def css():
    json_data = read_json('templates/css.json')
    return jsonify(json_data)

@app.route('/js/')
def js():
    json_data = read_json('templates/js.json')
    return jsonify(json_data)

@app.route('/ajax/')
def ajax():
    json_data = read_json('templates/ajax.json')
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

