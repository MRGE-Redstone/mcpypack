import pytest

from MCpypack.utils import Rarity

def test_values_contains_all_rarities():
    values = Rarity.values()

    expected = [
        "common",
        "uncommon",
        "rare",
        "epic",
    ]

    assert values == expected

@pytest.mark.parametrize("string, rarity", [
    ("common", Rarity.COMMON),
    ("uncommon", Rarity.UNCOMMON),
    ("rare", Rarity.RARE),
    ("epic", Rarity.EPIC),
])
def test_from_str_valid_values(string: str, rarity: Rarity):
    assert Rarity.from_str(string) == rarity

def test_from_str_invalid_value():
    with pytest.raises(ValueError):
        Rarity.from_str("invalid_rarity")
