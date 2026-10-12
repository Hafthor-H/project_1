
from injector import Module, provider, singleton

from structured_logging.command_queue.queue import Queue

from structured_logging.configuration.logger_config import LoggerConfig


class AppModule(Module):
    def __init__(self, logger_config: LoggerConfig) -> None:
        self.__logger_config = logger_config

    @provider
    @singleton
    def provide_logger_config(self) -> LoggerConfig:
        return self.__logger_config

    @provider
    @singleton
    def provide_queue(self) -> Queue:
        return Queue(
            self.__logger_config.async_wait_delay_in_seconds
        )
