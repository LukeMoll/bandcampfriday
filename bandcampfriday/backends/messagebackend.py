import abc

class AbstractMessageBackend(abc.ABC):

    @abc.abstractmethod
    def send_message(self, msg: str):
        pass