from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def error(self, message: str, exception: Exception = None, obj=None):
        pass

    @abstractmethod
    def warning(self, message: str, exception: Exception = None, obj=None):
        pass

    @abstractmethod
    def info(self, message: str, obj=None):
        pass
