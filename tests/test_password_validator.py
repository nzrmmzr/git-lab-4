
import pytest
from password_validator import password_ok


def test_valid_password_is_accepted():
    assert password_ok("Student123") is True


def test_password_shorter_than_8_characters_is_rejected():
    with pytest.raises(ValueError, match="Password cannot be less than 8 symbols"):
        password_ok("Abc1234")


def test_password_with_exactly_8_characters_is_accepted():
    assert password_ok("Abcdef12") is True


def test_password_longer_than_32_characters_is_rejected():
    password = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA13"

    with pytest.raises(ValueError, match="Password cannot be bigger than 32 symbols"):
        password_ok(password)


def test_password_with_exactly_32_characters_is_accepted():
    password = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1"

    assert password_ok(password) is True


def test_password_with_spaces_is_rejected():
    with pytest.raises(ValueError, match="Password cannot contain spaces"):
        password_ok("Abc 1234")


def test_password_without_letters_is_rejected():
    with pytest.raises(ValueError, match="Password needs to contain at least one letter"):
        password_ok("12345678")


def test_password_without_digits_is_rejected():
    with pytest.raises(ValueError, match="Password needs to contain at least one number"):
        password_ok("Abcdefgh")


def test_empty_password_is_rejected():
    with pytest.raises(ValueError, match="Password cannot be empty"):
        password_ok("")


def test_password_with_only_spaces_is_rejected():
    with pytest.raises(ValueError):
        password_ok("        ")



def test_password_with_multiple_violations_is_rejected():
    with pytest.raises(ValueError) as error:
        password_ok("abc ")

    message = str(error.value)
    assert "Password cannot be less than 8 symbols" in message
    assert "Password cannot contain spaces" in message
    assert "Password needs to contain at least one number" in message
