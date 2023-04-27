import abc


class Serviceable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def needs_service(self):
        pass
