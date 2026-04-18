# This file contains the custom_name component

from .components import ItemComponent
from MCpypack.utils import PlainText

class CustomName(ItemComponent):
    """
    Custom name item component.
    Used to specify an item, block, or entity's custom name. This component can be added, changed, or removed by any player with the item who has access to an anvil.
    """

    @property
    def TYPE(self) -> str:
        return "minecraft:custom_name"

    @property
    def custom_name(self) -> PlainText:
        return self._custom_name

    @custom_name.setter
    def custom_name(self, value: PlainText) -> None:
        if not isinstance(value, PlainText):
            raise ValueError(f"custom_name must be of type PlainText, got: {type(value)}")

        self._custom_name = value

    def __init__(self,
                 custom_name: PlainText,
                 ) -> None:
        super().__init__()

        self.custom_name = custom_name

    def to_value(self) -> dict:
        return self.custom_name.to_dict()
