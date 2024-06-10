from flask import Flask, render_template

app = Flask(__name__)

from users.views import  users_blueprint
from manage.views import manage_blueprint
app.register_blueprint(users_blueprint)
app.register_blueprint(manage_blueprint)


@app.route('/')
def index():  # put application's code here
    return render_template('main/index.html')


if __name__ == '__main__':
    app.run()
