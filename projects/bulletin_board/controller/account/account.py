from flask import Blueprint
from flask import render_template

account = Blueprint('account', __name__, url_prefix="/accounts")

@account.route('/manage_my_account/')
def manage_my_account():
    return render_template('accounts/manage_my_account.html')

