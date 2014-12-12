import json
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DB:
    def __init__(self):
        return

    @staticmethod
    def get_document(file_name):
        with open(file_name) as file_handle:
            return json.load(file_handle)
