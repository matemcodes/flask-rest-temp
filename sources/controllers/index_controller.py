from utils.log import log
from utils.close import exit_app
import services.index_service as service

try: from flask_restful import Resource
except ImportError as ex: exit_app(f"Module not found: {ex}")

class Index(Resource):
    def get(self):
        log.info('Getting index message')
        return service.get_index_message(), 200