from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify

signup = Blueprint('signup', __name__, url_prefix='/signup')
   
@signup.route('/', methods=['GET', 'POST'])
def signup_stage(): 
    if request.method == 'GET':
        return render_template('signup/signup.html')
    elif request.method == 'POST':
       data = request.form
       user_data = {"email": data['email'], "pw": data['pw'], "name": data['name']}
       print(user_data)
       return jsonify(user_data)

@signup.route('/verify_code/', methods=['POST'])
def verify_code():
    entered_verification = request.get_json()
    tmp_verification = '0000'
    if entered_verification['entered_verification'] == tmp_verification:
        return jsonify({"result": "True"})
    else:
        return jsonify({"result": "False"})
 
