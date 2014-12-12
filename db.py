import json
import logging
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DB:
    def __init__(self):
        return

    @staticmethod
    def get_document(file_name):
        script_dir = os.path.dirname(__file__) + '/'
        # logger.info(script_dir)
        with open(script_dir + file_name) as file_handle:
            data = json.load(file_handle)
            file_handle.close()
            return data
