from flask import Flask
from flask_restful import Api

from routes.services import Services

class Server:
    app = Flask(__name__)
    api = Api(app)

    def __init__(self, docker):
        self.docker = docker
        self.api.add_resource(Services, '/services', resource_class_kwargs={'docker': docker})

    @app.route("/")
    def hello():
        return "hello"

    def start_server(self):
        self.app.run(debug=True)
