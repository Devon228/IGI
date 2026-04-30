'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: color
Defines the Color class for storing and validating color names.
'''

class Color:
    """
    Class representing a color of a geometric figure.
    Uses property with getter and setter.
    """

    def __init__(self, color_name: str):
        """
        Initialize color with a name.

        Args:
            color_name (str): Name of the color (e.g., "red", "blue").
        """
        self._color = None
        self.color = color_name  

    @property
    def color(self) -> str:
        """Getter for color."""
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        """
        Setter for color with validation.
        Accepts any non-empty string (can be extended with a list of valid colors).

        Args:
            value (str): Color name.

        Raises:
            ValueError: If color name is empty.
        """
        if not value or not value.strip():
            raise ValueError("Color name cannot be empty")
        self._color = value.strip().lower()

    def __repr__(self) -> str:
        return f"Color('{self.color}')"