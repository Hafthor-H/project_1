from structured_logging.processors.abstract_processor import AbstractProcessor

class MaskingProcessor(AbstractProcessor):
    def __init__(self, mask: list) -> None:
        super().__init__()
        self.__mask = mask

    def process(self, data: dict):
        for key in self.__mask:
            data[key] = "***"