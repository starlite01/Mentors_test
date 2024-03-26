import pytest
from src.task import CustomDict


class TestMyDict:
    def test_create(self):
        created_custom_dict = CustomDict(20)
        assert created_custom_dict._table_size == 20
        assert created_custom_dict._data_dump == [None] * 20

    @pytest.mark.parametrize(
        "key, value",
        [
            ("uniq_key_1", 123),
            (1111, "value_1"),
            (("composite", "key"), "value"),
            (("super", "composite", 123), "value")
        ]
    )
    def test_setitem(self, custom_dict, key, value):
        custom_dict[key] = value
        assert custom_dict[key] == value

    def test_setitem_invalid_key(self, custom_dict):
        with pytest.raises(TypeError):
            custom_dict[[123, 25]] = "value..."

    def test_override(self, custom_dict):
        custom_dict[1] = "key_1"
        custom_dict[1.0] = "key_1.0"
        custom_dict[True] = "key_True"

        assert custom_dict[1] == "key_True"
        assert custom_dict[1.0] == "key_True"
        assert custom_dict[True] == "key_True"

    def test_getitem(self, custom_dict):
        custom_dict[10] = "mouse"
        assert custom_dict[10] == "mouse"

        with pytest.raises(KeyError):
            custom_dict["NotExistsKey"]

    def test_delete(self, custom_dict):
        custom_dict["key_to_delete"] = "value_to_delete"
        custom_dict["no_delete!"] = "value_not_delete!"

        del custom_dict["key_to_delete"]
        assert custom_dict["key_to_delete"] is None
        assert custom_dict["no_delete!"] == "value_not_delete!"
        del custom_dict["not_exists_key"]

    def test_presentation_view(self, custom_dict):
        custom_dict["test_key_name"] = "test_key_value"
        assert "{test_key_name: test_key_value}" == str(custom_dict)

    def test_keys(self, custom_dict):
        custom_dict["test_key_name_1"] = "test_key_value_1"
        custom_dict["test_key_name_2"] = "test_key_value_2"
        custom_dict["test_key_name_3"] = "test_key_value_3"

        expected_keys = [
            "test_key_name_3", "test_key_name_2", "test_key_name_1"
        ]
        keys = custom_dict.keys()
        for expected_key in expected_keys:
            assert expected_key in keys

    def test_values(self, custom_dict):
        custom_dict["test_key_name_1"] = 123
        custom_dict["key_test_2_name"] = "test_key_value_2"
        custom_dict["3_name_key_test"] = ["apple", "orange", ""]

        expected_values = [
            123, "test_key_value_2", ["apple", "orange", ""]
        ]
        values = custom_dict.values()

        for expected_value in expected_values:
            assert expected_value in values

    def test_items(self, custom_dict):
        custom_dict["test_key_name_1"] = 123
        custom_dict["key_test_2_name"] = "test_key_value_2"
        custom_dict["3_name_key_test"] = ["apple", "orange", ""]

        expected_items = [
            ('3_name_key_test', ['apple', 'orange', '']),
            ('test_key_name_1', 123),
            ('key_test_2_name', 'test_key_value_2')
        ]
        items = custom_dict.items()

        for expected_item in expected_items:
            assert expected_item in items
