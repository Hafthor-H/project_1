from client.infrastructure.logging.i_logger import ILogger
from injector import inject
from structured_logging.logger.logger import Logger

class LoggingAdapter(ILogger):
    @inject
    def __init__(self, logger: Logger) -> None:
        self.__logger = logger

    def error(self, message: str, exception: Exception = None):
        self.__logger.log(message=message,exception=exception)

    def warning(self, message: str, exception: Exception = None):
        self.__logger.log(message=message,exception=exception)

    def info(self, message: str):
        self.__logger.log(message=message)
