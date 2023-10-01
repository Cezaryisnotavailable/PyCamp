from abc import ABC, abstractmethod
from project import check_password


class Validator(ABC):
    @abstractmethod
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def is_valid(self):
        pass


class HasNumberValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        for n in range(0, 10):
            if str(n) in self.text:
                return True
        return False


class LengthValidator(Validator):
    def __init__(self, text, min_length=8):
        self.text = text
        self.min_length = min_length

    def is_valid(self):
        return len(self.text) >= self.min_length


class HasSpecialCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        for char in self.text:
            if not char.isalnum():
                return True
        return False


class HasUpperCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        for char in self.text:
            if char.isupper():
                return True
        return False


class HasLowerCharacterValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        for char in self.text:
            if char.islower():
                return True
        return False


class HaveIbeenPwnedValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        return check_password(self.text)


class PasswordValidator(Validator):
    def __init__(self, password):
        self.password = password
        self.validators = [
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharacterValidator,
            HasUpperCharacterValidator,
            HasLowerCharacterValidator,
            HaveIbeenPwnedValidator,
        ]

    def is_valid(self):
        for class_name in self.validators:
            validator = class_name(self.text)
            validator.is_valid()


# validator = PasswordValidator("asdas3")
# print(validator.is_valid())