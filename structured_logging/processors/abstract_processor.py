from i_processor import IProcessor

class AbstractProcessor(IProcessor):
    def __init__(self) -> None:
        self._next_processor = None

    def set_next(self, processor: IProcessor):
        self._next_processor = processor

    def handle(self, data: dict):

        self.process(data)

        if self._next_processor is not None:
            self._next_processor.handle(data)

    def process(self, data: dict):
        pass