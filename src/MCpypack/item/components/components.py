# This file contains the ItemComponent class

from abc import abstractmethod, ABC

class ItemComponents:
    """
    Item components.
    """

    def __init__(self, *components: ItemComponent) -> None:
        """
        Init new components for an item.

        Parameters
        ----------
        *components:
            Components to add.
        """

        self.config: dict[str, dict[str, str]] = {}

        for component in components:
            self.config[f"{component.TYPE}"] = component.to_dict()

class ItemComponent(ABC):
    """
    Item component.
    """

    @property
    @abstractmethod
    def TYPE(self) -> str:
        """
        Return the type of the item component.
        """
        pass

    def __init__(self) -> None:
        """
        New item component.
        """

        self.config: dict[str, str]

    @abstractmethod
    def to_dict(self) -> dict[str, str]:
        """
        Convert component to dictionary.
        """

