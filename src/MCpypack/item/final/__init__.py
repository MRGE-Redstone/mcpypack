# Export Item enum
# Export Tags enum
# Export TrimPattern enum
# Export Enchantment enum
# Export DamageType enum

from .items import Item
from.tags import Tag
from.trim_patterns import TrimPattern
from .enchantments import Enchantment
from .damage_types import DamageType

type ItemLike = Item | Tag.ITEM | list[Item] | list[Tag.ITEM] | list[Item | Tag.ITEM]

__all__: list[str] = [
    "Item",
    "Tag",
    "ItemLike",
    "TrimPattern",
    "Enchantment",
    "DamageType",
]
