'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: task6b
Pandas analysis of Melbourne Housing dataset.
Task: Compare average price for max rooms vs min rooms.
'''

import pandas as pd
from common.task import Task
from common.action import Action


class Task6b(Task):
    name = "Task 6b: Melbourne Housing Analysis"

    def __init__(self):
        self.df = None

    def menu_text(self) -> str:
        if self.df is not None:
            return f"Dataset loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns"
        else:
            return "No dataset. Please load Melbourne Housing CSV."

    def actions(self):
        return super().actions() + [
            Action("Load Melbourne Housing CSV", self.load_data),
            Action("Show basic info", self.show_info),
            Action("Compute price ratio (max rooms / min rooms)", self.price_ratio),
        ]

    def load_data(self):
        """Load Melbourne housing dataset from CSV file."""
        file_path = "/home/dimas/University/sem 4/IGI/LR4/task6/Melbourne_housing.csv"
        if not file_path:
            file_path = "/home/dimas/University/sem 4/IGI/LR4/task6/Melbourne_housing.csv"
        try:
            self.df = pd.read_csv(file_path)
            print(f"Loaded {len(self.df)} records.")
        except FileNotFoundError:
            print("File not found. Please download the dataset from Kaggle.")
        except Exception as e:
            print(f"Error: {e}")

    def show_info(self):
        """Display basic information about the DataFrame."""
        if self.df is None:
            print("No data loaded.")
            return
        print("\n=== DataFrame Info ===")
        print(f"Shape: {self.df.shape}")
        print("\nColumn names and types:")
        print(self.df.dtypes)
        print("\nFirst 5 rows:")
        print(self.df.head())
        print("\nBasic statistics (numeric columns):")
        print(self.df.describe())

    def price_ratio(self):
        """Compute ratio: average price for max rooms / average price for min rooms (rooms > 0)."""
        if self.df is None:
            print("No data loaded.")
            return

        # Ensure necessary columns exist
        if 'Rooms' not in self.df.columns or 'Price' not in self.df.columns:
            print("Required columns 'Rooms' or 'Price' not found in dataset.")
            return

        # Filter out rows where Rooms is NaN or <= 0 (but rooms are positive integers)
        valid = self.df.dropna(subset=['Rooms', 'Price'])
        valid = valid[valid['Rooms'] > 0]

        if valid.empty:
            print("No valid data after filtering.")
            return

        # Find max and min rooms
        max_rooms = valid['Rooms'].max()
        min_rooms = valid['Rooms'].min()

        # Calculate average price for each group
        avg_price_max = valid[valid['Rooms'] == max_rooms]['Price'].mean()
        avg_price_min = valid[valid['Rooms'] == min_rooms]['Price'].mean()

        if avg_price_min == 0:
            print("Average price for min rooms is zero, cannot compute ratio.")
            return

        ratio = avg_price_max / avg_price_min
        print(f"\nMaximum number of rooms: {max_rooms}")
        print(f"Minimum number of rooms (>0): {min_rooms}")
        print(f"Average price for {max_rooms} rooms: ${avg_price_max:.2f}")
        print(f"Average price for {min_rooms} rooms: ${avg_price_min:.2f}")
        print(f"Ratio (max_rooms_avg / min_rooms_avg): {ratio:.2f}")

        # Store result for later use if needed
        self.result_ratio = round(ratio, 2)