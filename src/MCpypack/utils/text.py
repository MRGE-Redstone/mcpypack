# This file contains classes for the Minecraft text component.
# It represents a Minecraft text.
# The text component format is used for rich-text formatting.
# See more on https://minecraft.wiki/w/Text_component_format

from MCpypack.utils import TextColor, HexColor

class Formatting:
    """
    Class for text formatting.
    """

    @property
    def color(self) -> HexColor | TextColor:
        return self._color

    @color.setter
    def color(self, value: HexColor | TextColor) -> None:
        if not isinstance(value, HexColor | TextColor):
            raise ValueError(f"color must be of type HexColor | TextColor, got: {type(value)}")

        self._color = value

    @property
    def bold(self) -> bool:
        return self._bold

    @bold.setter
    def bold(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"bold must be of type bool, got: {type(value)}")

        self._bold = value

    @property
    def italic(self) -> bool:
        return self._italic

    @italic.setter
    def italic(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"italic must be of type bool, got: {type(value)}")

        self._italic = value

    @property
    def underlined(self) -> bool:
        return self._underlined

    @underlined.setter
    def underlined(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"underlined must be of type bool, got: {type(value)}")

        self._underlined = value

    @property
    def strikethrough(self) -> bool:
        return self._strikethrough

    @strikethrough.setter
    def strikethrough(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"strikethrough must be of type bool, got: {type(value)}")

        self._strikethrough = value

    @property
    def obfuscated(self) -> bool:
        return self._obfuscated

    @obfuscated.setter
    def obfuscated(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError(f"obfuscated must be of type bool, got: {type(value)}")

        self._obfuscated = value

    @property
    def shadow_color(self) -> int:
        return self._shadow_color

    @shadow_color.setter
    def shadow_color(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"shadow_color must be of type int, got: {type(value)}")

        if value < 0:
            raise ValueError(f"shadow_color must be at least 0, got: {value}")

        self._shadow_color = value

    def __init__(self,
                 *,
                 color: HexColor | TextColor,
                 bold: bool,
                 italic: bool,
                 underlined: bool,
                 strikethrough: bool,
                 obfuscated: bool,
                 shadow_color: int,
                 ) -> None:
        """
        Init text formatting object.
        """
        
        self.color = color
        self.bold = bold
        self.italic = italic
        self.underlined = underlined
        self.strikethrough = strikethrough
        self.obfuscated = obfuscated
        self.shadow_color = shadow_color

class PlainText:
    """
    Class representing texts components of the type 'text'.
    """
