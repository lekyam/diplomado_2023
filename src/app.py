from flask import Flask, render_template
from flask_cors import CORS
from config import config
from flask_restplus import Api, Resource

# Routes
from controllers import UserController, StatusController

app = Flask(__name__)
app = Api(app)
CORS(app, resources={"*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template('index.html')


def page_not_found(error):
    return "<h1>Not Found Page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(UserController.main, url_prefix='/users')
    app.register_blueprint(StatusController.main, url_prefix='/status')

    app.register_error_handler(404, page_not_found)
    app.run()
