from injector import Module, provider, singleton
from structured_logging.logger.logger import Logger
from structured_logging.logger_creation.logger_config_builder import LoggerConfigBuilder
from structured_logging.logger_creation.logger_factory import create_logger

from client.infrastructure.logging.i_logger import ILogger
from client.infrastructure.settings.settings import Settings
from client.infrastructure.logging.logger_config_factory import create_logger_config
from client.infrastructure.logging.logging_adapter import LoggingAdapter

class AppModule(Module):
    def __init__(self, settings: Settings) -> None:
        self.__settings = settings


    @provider
    @singleton
    def provide_logger(self) -> ILogger:
        config = create_logger_config(
        self.__settings,
        LoggerConfigBuilder()
        )

        logger = create_logger(config)
        return LoggingAdapter(logger)