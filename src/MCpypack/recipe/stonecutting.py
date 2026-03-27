from typing import Any

from MCpypack.item import Item

from .utils import Result
from .recipe import Recipe

class Stonecutting(Recipe):
    """
    Stonecutting recipe.
    """

    def __init__(self,
                 name: str,
                 ingredient: Item,
                 result: Result,
                 ) -> None:
        """
        Init stonecutting recipe.

        Parameters
        ----------
        name:
            Name of the recipe.
        ingredient:
            Ingredient of the stonecutting.
        result:
            Result of the crafting stored as a Result instance.
        """
        super().__init__(name)

        self.config: dict[str, str | dict] = {"type": "minecraft:stonecutting",
                             "ingredient" : ingredient.value,
                             "result" : result.to_dict()}

