from utils.log import log
from utils.close import exit_app
from models.example import Example, db

try: from flask_restful import Resource, reqparse
except ImportError as ex: exit_app(f"Module not found: {ex}")

parser = reqparse.RequestParser()
parser.add_argument('message')

class ExGetPost(Resource):
    def get(self):
        log.info('Getting examples')
        examples = Example.query.all()
        return [example.message for example in examples], 200

    def post(self):
        args = parser.parse_args()
        log.info('Creating a new example')
        example = Example(message=args['message'])

        db.session.add(example); db.session.commit()
        return f"Example created: {example.message}", 201