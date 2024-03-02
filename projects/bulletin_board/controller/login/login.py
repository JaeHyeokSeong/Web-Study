from flask import Blueprint
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session
from flask import jsonify
from model.user.user import User
import secrets

login = Blueprint('login', __name__, url_prefix='/nid')
login.secret_key = secrets.token_hex()

@login.route('/login/', methods=['GET', 'POST'])
def login_stage():
    if request.method == 'GET':
        return render_template('login/login.html')
    elif request.method == 'POST':
        data = request.form
        user = User(data['email'], data['pw'])        
        session['user'] = user.__dict__
        return redirect(url_for('index'))  

@login.route('/logout/')
def logout_stage():
    session.pop('user', None)
    return redirect(url_for('index'))

@login.route('/find_password/', methods=['GET', 'POST'])
def find_password():
    if request.method == 'GET':
        return render_template('login/find_password.html')
    elif request.method == 'POST':
        email = request.form['email']
        return jsonify({'email': email})


