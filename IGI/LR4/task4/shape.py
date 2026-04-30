'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: shape
Defines abstract base class Shape and its descendants: Rectangle and Square.
'''

from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from .color import Color

class Shape(ABC):
    """
    Abstract base class for all geometric figures.
    Requires implementation of area() method.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.
        Must be overridden in child classes.
        """
        pass

    @abstractmethod
    def get_params(self) -> str:
        """
        Return a formatted string with shape parameters, color, and area.
        Must be overridden.
        """
        pass

    @abstractmethod
    def draw(self, label: str, ax=None):
        """
        Draw the shape on a matplotlib axis.
        If ax is None, create a new figure and show.
        """
        pass

    def save(self, label: str, filename: str):
        """Save the shape drawing to a file."""
        fig, ax = plt.subplots(figsize=(6, 6))
        self.draw(label, ax)
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()


class Rectangle(Shape):
    """
    Rectangle figure with width, height, and color.
    """


    figure_type = "Rectangle"

    def __init__(self, width: float, height: float, color: Color):
        """
        Initialize rectangle.

        Args:
            width (float): Width of rectangle (positive).
            height (float): Height of rectangle (positive).
            color (Color): Color object.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers")
        self.width = width
        self.height = height
        self.color = color

    def area(self) -> float:
        """Calculate area of rectangle."""
        return self.width * self.height

    def get_params(self) -> str:
        """
        Return formatted string with rectangle parameters.
        Uses .format() method as required.
        """
        return ("Figure: {type}\n"
                "Width: {w:.2f}\n"
                "Height: {h:.2f}\n"
                "Color: {c}\n"
                "Area: {a:.2f}").format(
                    type=self.figure_type,
                    w=self.width,
                    h=self.height,
                    c=self.color.color,
                    a=self.area()
                )

    def draw(self, label: str, ax=None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))
            show_plot = True
        else:
            show_plot = False

        rect = patches.Rectangle((0, 0), self.width, self.height,
                                 linewidth=2, edgecolor='black',
                                 facecolor=self.color.color, alpha=0.7)
        ax.add_patch(rect)
        ax.set_xlim(-1, self.width + 1)
        ax.set_ylim(-1, self.height + 1)
        ax.text(self.width/2, self.height/2, label,
                ha='center', va='center', fontsize=12, color='black',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
        ax.axhline(0, color='gray', linewidth=0.5)
        ax.axvline(0, color='gray', linewidth=0.5)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.set_title(f"{self.figure_type} - {label}")

        if show_plot:
            plt.show()

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color.color})"


class Square(Rectangle):
    """
    Square – a special case of rectangle with equal sides.
    Inherits from Rectangle.
    """

    figure_type = "Square"

    def __init__(self, side: float, color: Color):
        """
        Initialize square.

        Args:
            side (float): Side length (positive).
            color (Color): Color object.
        """
        super().__init__(side, side, color)   # call parent constructor
        self.side = side

    @classmethod
    def circumscribed_about_circle(cls, radius: float, color: Color):
        """
        Create a square circumscribed about a circle of given radius.
        Side = 2 * radius.

        Args:
            radius (float): Radius of the inscribed circle.
            color (Color): Color of the square.

        Returns:
            Square: Square object.
        """
        side = 2 * radius
        return cls(side, color)

    def get_params(self) -> str:
        """Override to show side instead of width/height."""
        return ("Figure: {type}\n"
                "Side: {s:.2f}\n"
                "Color: {c}\n"
                "Area: {a:.2f}").format(
                    type=self.figure_type,
                    s=self.side,
                    c=self.color.color,
                    a=self.area()
                )

    def draw(self, label: str, ax=None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))
            show_plot = True
        else:
            show_plot = False

        square = patches.Rectangle((0, 0), self.side, self.side,
                                   linewidth=2, edgecolor='black',
                                   facecolor=self.color.color, alpha=0.7)
        ax.add_patch(square)
        ax.set_xlim(-1, self.side + 1)
        ax.set_ylim(-1, self.side + 1)
        ax.text(self.side/2, self.side/2, label,
                ha='center', va='center', fontsize=12, color='black',
                bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
        ax.axhline(0, color='gray', linewidth=0.5)
        ax.axvline(0, color='gray', linewidth=0.5)
        ax.set_aspect('equal')
        ax.grid(True, linestyle=':', alpha=0.5)
        ax.set_title(f"{self.figure_type} - {label}")

        if show_plot:
            plt.show()

    def __repr__(self) -> str:
        return f"Square(side={self.side}, color={self.color.color})"