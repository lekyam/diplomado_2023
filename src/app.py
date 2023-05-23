from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api
from src.routes import User, Status


app = Flask(__name__)


CORS(app, resources={"*": {"origins": "*"}})

api = Api(app)


def page_not_found(error):
    return render_template('NotFound.html'), 404


api.add_namespace(User.user_namespace)
api.add_namespace(Status.status_namespace)
app.register_blueprint(User.main, url_prefix='/users')
app.register_blueprint(Status.main, url_prefix='/status')

app.register_error_handler(404, page_not_found)


application = app
if __name__ == '__main__':
    application.run(debug=True)
