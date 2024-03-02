from flask import Flask
from flask import render_template
from controller.account import account
from controller.signup import signup
from controller.login import login 

app = Flask(__name__)
app.register_blueprint(account.account)
app.register_blueprint(signup.signup)
app.register_blueprint(login.login)
app.secret_key = login.login.secret_key

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True, port=8000) 

