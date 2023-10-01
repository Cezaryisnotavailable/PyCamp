from abc import ABC, abstractmethod
from project import check_password_if_leaked, logger


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
        return check_password_if_leaked(self.text)


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
            class_validator = class_name(self.password)
            result = class_validator.is_valid()
            logger.info(f"class_name {class_name.__name__} result {result}")


if __name__ == "__main__":
    validator = PasswordValidator("asdas3")
    validator.is_valid()
    logger.info("---" * 2 + "New password checking".upper() + "---" * 2)
    validator = PasswordValidator("asdasdSS@#$#@8274023!(())&^%$#asdasdXCFDYH")
    validator.is_valid()
