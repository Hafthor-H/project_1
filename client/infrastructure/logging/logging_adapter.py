from client.infrastructure.logging.i_logger import ILogger
from injector import inject
from structured_logging.logger.logger import Logger

class LoggingAdapter(ILogger):
    @inject
    def __init__(self, logger: Logger) -> None:
        self.__logger = logger

    def error(self, message: str, exception: Exception = None, obj = None):
        data = self.__data(message=message,level="Error", obj=obj, exception=exception)
        self.__logger.log(**data)

    def warning(self, message: str, exception: Exception = None, obj = None):
        data = self.__data(message=message,level="Warning", obj=obj, exception=exception)
        self.__logger.log(**data)

    def info(self, message: str,  obj = None):
        data = self.__data(message=message,level="Info", obj=obj)
        self.__logger.log(**data)

    def __data(self, message: str, level: str, exception: Exception = None, obj = None) -> dict:
        data = {'message': message, 'Level': level}
        if exception is not None:
                    data['exception'] = exception
        if obj is not None:
                    data |= obj.__dict__

        return data

        