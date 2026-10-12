from structured_logging.processors.abstract_processor import AbstractProcessor

class EnvironmentProcessor(AbstractProcessor):
    def __init__(self, environment):
        super().__init__()
        self._environment = environment

    def process(self, data):
        data["environment"] = self._environment.value