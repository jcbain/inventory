from flask_restful import Resource

class Services(Resource):
    def __init__(self, **kwargs):
        self.docker = kwargs['docker']

    def get(self):
        container = self.docker.run_container('server')
        return {'name': 'hello'}
    

