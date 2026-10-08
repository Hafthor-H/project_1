import threading
import time
from structured_logging.command_queue.command import Command



class Queue:
    # TODO: we also need to inject the async delay time into the constructor
    def __init__(self, async_wait_delay_in_seconds: int):

        self.__commands: list[Command] = []
        self.__async_wait_delay_in_seconds = async_wait_delay_in_seconds
        self.__thread = threading.Thread(target=self.__process)
        self.__thread.daemon = True
        self.__thread.start()

    def add(self, command: Command):

        self.__commands.append(command)

    def __process(self):

        while True:
            if not self.__commands:
                time.sleep(self.__async_wait_delay_in_seconds)
                continue
            command = self.__commands.pop(0)
            command.execute()