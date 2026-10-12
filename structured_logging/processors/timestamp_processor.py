from structured_logging.processors.abstract_processor import AbstractProcessor
from datetime import datetime


class TimestampProccessor(AbstractProcessor):
    def process(self, data: dict):
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data["timestamp"] = time
