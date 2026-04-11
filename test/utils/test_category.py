import pytest

from MCpypack.utils import Category

def test_values_contains_all_categories():
    values = Category.values()

    expected = [
        "equipment",
        "building",
        "misc",
        "redstone",
    ]

    assert values == expected

@pytest.mark.parametrize("string, category", [
    ("building", Category.BUILDING),
    ("equipment", Category.EQUIPMENT),
    ("misc", Category.MISC),
    ("redstone", Category.REDSTONE),
])
def test_from_str_valid_values(string: str, category: Category):
    assert Category.from_str(string) == category

def test_from_str_invalid_value():
    with pytest.raises(ValueError):
        Category.from_str("invalid_category")
