from structured_logging.configuration.environment import Environment
from structured_logging.configuration.logger_config import LoggerConfig
from structured_logging.processors.i_processor import IProcessor
from structured_logging.sinks.i_sink import ISink
from structured_logging.sinks.file_sink import FileSink
from structured_logging.sinks.console_sink import ConsoleSink
from structured_logging.processors.null_processor import NullProcessor
from structured_logging.processors.environment_processor import EnvironmentProcessor

class LoggerConfigBuilder:
    def __init__(self):
        self._sink : ISink = ConsoleSink()
        self._is_async : bool = False
        self._async_wait_delay_in_seconds : int = 0
        self._processor : IProcessor = NullProcessor()
        self._last_processor : IProcessor| None  = None

    def with_custom_sink(self, sink: ISink) -> 'LoggerConfigBuilder':
        self._sink = sink
        return self

    def with_file_sink(self, file_path: str) -> 'LoggerConfigBuilder':
        self._sink = FileSink(file_path)
        return self

    def with_console_sink(self) -> 'LoggerConfigBuilder':
        self._sink = ConsoleSink()
        return self

    def as_async(self, wait_delay_in_seconds: int) -> 'LoggerConfigBuilder':
        self._is_async = True
        self._async_wait_delay_in_seconds = wait_delay_in_seconds
        return self

    def add_environment(self, environment: Environment) -> 'LoggerConfigBuilder':
        processor = EnvironmentProcessor(environment)
        self.add_processor(processor)
        return self

    def add_processor(self, processor: IProcessor) -> 'LoggerConfigBuilder':
        if self._last_processor is None:
            self._processor = processor
            self._last_processor = processor
        else:
            self._last_processor.set_next(processor)
            self._last_processor = processor

        return self

    def _clear(self):
        self._sink = ConsoleSink()
        self._processor = NullProcessor()
        self._is_async = False
        self._async_wait_delay_in_seconds = 0
        self._last_processor = None

    def build(self) -> LoggerConfig:
        config = LoggerConfig(
            sink = self._sink,
            processor=self._processor,
            async_wait_delay_in_seconds= self._async_wait_delay_in_seconds,
            is_async=self._is_async
        )
        self._clear()

        return config
