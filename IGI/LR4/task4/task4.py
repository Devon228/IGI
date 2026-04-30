'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: task4
Implements Task4: geometric shapes with user input, plotting, and file output.
'''

import os
from common.task import Task
from common.action import Action
from common.ui import read_float, read_str
from .color import Color
from .shape import Rectangle, Square


class Task4(Task):
    """
    Task 4: Work with geometric shapes (Rectangle, Square circumscribed about a circle).
    Allows user to input parameters, displays shape with chosen color and text label,
    saves plot to file.
    """
    name = "Task 4: Geometric Shapes"

    def __init__(self):
        self.shape = None
        self.text_label = ""

    def menu_text(self) -> str:
        if self.shape:
            return f"Current shape:\n{self.shape.get_params()}"
        else:
            return "No shape created yet. Please create a shape."

    def actions(self):
        return super().actions() + [
            Action("Create Rectangle", self.create_rectangle),
            Action("Create Square circumscribed about a circle", self.create_square_from_circle),
            Action("Draw shape (with label)", self.draw_shape),
            Action("Save shape to file", self.save_to_file),
        ]

    def create_rectangle(self):
        """Prompt user for rectangle dimensions and color."""
        try:
            width = read_float("Enter width (positive): ", min=0.0001)
            height = read_float("Enter height (positive): ", min=0.0001)
            color_name = read_str("Enter color (e.g., red, blue, green): ")
            color = Color(color_name)
            self.shape = Rectangle(width, height, color)
            self.text_label = read_str("Enter label text for the shape: ")
            print("Rectangle created successfully.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def create_square_from_circle(self):
        """Create a square circumscribed about a circle of given radius."""
        try:
            radius = read_float("Enter circle radius R (positive): ", min=0.0001)
            color_name = read_str("Enter color for the square: ")
            color = Color(color_name)
            self.shape = Square.circumscribed_about_circle(radius, color)
            self.text_label = read_str("Enter label text for the square: ")
            print(f"Square created: side = {self.shape.side:.2f}, area = {self.shape.area():.2f}")
        except ValueError as e:
            print(f"Invalid input: {e}")

    def draw_shape(self):
        if self.shape is None:
            print("No shape to draw.")
            return
        self.shape.draw(self.text_label)

    def save_to_file(self):
        if self.shape is None:
            print("No shape to save.")
            return
        os.makedirs("results", exist_ok=True)
        filename = f"results/{self.shape.figure_type}_{self.shape.color.color}.png"
        filename = filename.replace(' ', '_')
        self.shape.save(self.text_label, filename)
        print(f"Saved to {filename}")