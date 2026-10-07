from structured_logging.processors.abstract_processor import AbstractProcessor
from datetime import datetime, timezone


class TimestampProccessor(AbstractProcessor):
    def process(self, data: dict):
        time = datetime.now(timezone.utc).isoformat()
        data["timestamp"] = time
