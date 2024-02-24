from flask import Flask, jsonify, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('json_practise.html')

@app.route('/ajaxPost/', methods=['POST'])
def ajax_post():
    data = request.get_json()
    return jsonify(data)

@app.route('/ajaxGet/')
def ajax_get():
    # get 일때에는 json 을 받기위해서는 request.args 를 사용한다.
    data = request.args
    print(data)
    now = datetime.now()
    time = {
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second
        }  
    return jsonify(time)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
