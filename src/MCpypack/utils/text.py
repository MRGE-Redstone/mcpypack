# This file contains classes for the Minecraft text component.
# It represents a Minecraft text.
# The text component format is used for rich-text formatting.
# See more on https://minecraft.wiki/w/Text_component_format

from MCpypack.utils import Color

class Formatting:
    """
    Class for text formatting.
    """

    def __init__(self,
                 *,
                 color: Color,
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
        pass

class PlainText:
    """
    Class representing texts components of the type 'text'.
    """
