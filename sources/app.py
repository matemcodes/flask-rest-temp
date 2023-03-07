from models import db
from utils.log import log
from create import api, app
from utils.env import get_env
from utils.close import exit_app

try:
    from waitress import serve
    from sqlalchemy_utils import database_exists
    from sqlalchemy_utils import create_database
except ImportError as import_error:
    exit_app(f"Module not found: {import_error}")

import controllers.index_controller as indx_ctrl
import controllers.example_controller as exmp_ctrl

api.add_resource(indx_ctrl.Index, '/')
api.add_resource(exmp_ctrl.ExGetPost, '/example')

with app.app_context():
    db.init_app(app)
    engine = db.engine.url

    try:
        if not database_exists(engine):
            create_database(engine)
        db.create_all()
        log.info("Db created")
    except Exception as db_error:
        exit_app(f"Db error: {db_error}")

if __name__ == '__main__':
    log.debug("Starting app")
    host_port = get_env("HOST_PORT")
    host_address = get_env("HOST_ADDRESS")

    if (get_env("DEBUG") != "True"):
        serve(app, port=host_port, host=host_address)
    else: app.run(port=host_port, host=host_address, debug=True)