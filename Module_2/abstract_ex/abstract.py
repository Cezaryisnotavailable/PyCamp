from abc import ABC, abstractmethod


class ValidatorInterface(ABC):
    @abstractmethod
    def validate(self):
        pass


class Validator(ValidatorInterface):
    def validate(self):
        return 0


validator = Validator()
