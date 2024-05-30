import pytest
from utils import string_to_boolean


class TestStringToBoolean:
    @pytest.mark.parametrize(
        "value, expected",
        [
            ("true", True),
            ("false", False),
            ("t", True),
            ("f", False),
            ("1", True),
            ("0", False),
            ("", False),
            (None, False),
        ],
    )
    def test_string_to_boolean_should_return_correct_boolean_value(
        self, value, expected
    ):
        result = string_to_boolean(value)
        assert result == expected
        assert type(result) == bool

    def test_string_to_boolean_should_raise_value_error_when_value_is_invalid(self):
        with pytest.raises(ValueError) as e:
            string_to_boolean("invalid")

        assert str(e.value) == "invalid is not a valid boolean value"
