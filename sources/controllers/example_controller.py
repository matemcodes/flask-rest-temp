from utils.log import log
from utils.close import exit_app
import services.example_service as service

try: from flask_restful import Resource, reqparse
except ImportError as ex: exit_app(f"Module not found: {ex}")

parser = reqparse.RequestParser()
parser.add_argument('message')

class ExGetPost(Resource):
    def get(self):
        log.info('Getting examples')
        return service.get_all_example(), 200

    def post(self):
        args = parser.parse_args()
        log.info('Creating a new example')
        return service.create_new_example(args), 201