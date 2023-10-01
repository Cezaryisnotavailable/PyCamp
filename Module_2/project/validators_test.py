from validators import HasNumberValidator, HasSpecialCharacterValidator, HasUpperCharacterValidator, \
    HasLowerCharacterValidator, LengthValidator, HaveIbeenPwnedValidator


def test_if_has_number_validator_positive():
    validator = HasNumberValidator("abc1")
    assert validator.is_valid() is True


def test_if_has_number_validator_negative():
    validator = HasNumberValidator("abc")
    assert validator.is_valid() is False


def test_if_has_special_character_validator_positive():
    validator = HasSpecialCharacterValidator("ab$&c1")
    assert validator.is_valid() is True


def test_if_has_special_character_validator_negative():
    validator = HasSpecialCharacterValidator("abc")
    assert validator.is_valid() is False


def test_if_has_upper_character_validator_positive():
    validator = HasUpperCharacterValidator("ab$&c1D")
    assert validator.is_valid() is True


def test_if_has_upper_character_validator_negative():
    validator = HasUpperCharacterValidator("abc")
    assert validator.is_valid() is False


def test_if_has_lower_character_validator_positive():
    validator = HasLowerCharacterValidator("ab$&c1D")
    assert validator.is_valid() is True


def test_if_has_lower_character_validator_negative():
    validator = HasLowerCharacterValidator("TTTT")
    assert validator.is_valid() is False


def test_if_length_validator_positive():
    validator = LengthValidator("ab$&c1Dasdsad")
    assert validator.is_valid() is True

    validator = LengthValidator("ab$", 3)
    assert validator.is_valid() is True


def test_if_length_validator_negative():
    validator = LengthValidator("TTTT")
    assert validator.is_valid() is False

    validator = LengthValidator("TTTT, 5")
    assert validator.is_valid() is False


def test_pwned_validator():
    validator = HaveIbeenPwnedValidator("TTTT!@#!@#3412412421asdasd")
    assert validator.is_valid() is True

    validator = HaveIbeenPwnedValidator("TTTT")
    assert validator.is_valid() is False

