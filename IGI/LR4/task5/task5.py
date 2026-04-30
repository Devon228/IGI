'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.


Module: task5
Demonstrates NumPy capabilities: array creation, indexing, slicing,
universal functions, and statistical operations (mean, median, corrcoef,
var, std). Also computes sum below main diagonal and std of diagonal
elements (two ways).
'''

import numpy as np
from common.task import Task
from common.action import Action
from common.ui import read_int


class Task5(Task):
    name = "Task 5: NumPy Matrix Analysis"

    def __init__(self):
        self.matrix = None  
        self.n = 0
        self.m = 0

    def menu_text(self) -> str:
        if self.matrix is not None:
            return f"Matrix shape: {self.n} x {self.m}\nValues: 0..100"
        else:
            return "No matrix generated. Please generate one."

    def actions(self):
        return super().actions() + [
            Action("Generate random integer matrix", self.generate_matrix),
            Action("Show matrix", self.show_matrix),
            Action("Sum below main diagonal", self.sum_below_diag),
            Action("Std of diagonal (two ways)", self.std_diagonal),
            Action("Statistical summary (mean, median, var, std, corrcoef)", self.statistics),
            Action("Demonstrate indexing and slicing", self.demo_indexing),
        ]

    def generate_matrix(self):
        """Generate random integer matrix A[n, m] using NumPy."""
        self.n = read_int("Enter number of rows n: ", min=1, max=20)
        self.m = read_int("Enter number of columns m: ", min=1, max=20)
        self.matrix = np.random.randint(0, 101, size=(self.n, self.m))
        print(f"Generated {self.n}x{self.m} matrix with integers 0..100.")

    def show_matrix(self):
        if self.matrix is None:
            print("No matrix. Generate first.")
            return
        print("\nMatrix A:")
        print(self.matrix)

    def sum_below_diag(self):
        if self.matrix is None:
            print("No matrix.")
            return
        below = np.tril(self.matrix, k=-1)
        total = np.sum(below)
        print(f"Sum of elements below main diagonal: {total}")

    def std_diagonal(self):
        if self.matrix is None:
            print("No matrix.")
            return
        diag = np.diag(self.matrix)
        if len(diag) == 0:
            print("Matrix has no diagonal elements?")
            return

        std_builtin = np.std(diag)
        mean_val = np.mean(diag)
        squared_diff = (diag - mean_val) ** 2
        variance_manual = np.sum(squared_diff) / len(diag)
        std_manual = np.sqrt(variance_manual)

        print(f"Diagonal elements: {diag}")
        print(f"Standard deviation (built-in np.std): {std_builtin:.2f}")
        print(f"Standard deviation (manual formula): {std_manual:.2f}")

    def statistics(self):
        if self.matrix is None:
            print("No matrix.")
            return

        flat = self.matrix.flatten()

        print("\n=== Statistical summary ===")
        print(f"Mean (all elements): {np.mean(flat):.4f}")
        print(f"Median (all elements): {np.median(flat):.4f}")
        print(f"Variance (all elements, ddof=0): {np.var(flat):.4f}")
        print(f"Standard deviation (all elements, ddof=0): {np.std(flat):.4f}")

        # Correlation coefficient between rows 1 ans 2
        if self.n >= 2:
            row0 = self.matrix[0, :]
            row1 = self.matrix[1, :]
            corr = np.corrcoef(row0, row1)[0, 1]
            print(f"Correlation coefficient between row 0 and row 1: {corr:.4f}")
        else:
            print("Not enough rows for correlation (need at least 2).")

        # Correlation coefficient between columns 1 and 2
        if self.m >= 2:
            col0 = self.matrix[:, 0]
            col1 = self.matrix[:, 1]
            corr_col = np.corrcoef(col0, col1)[0, 1]
            print(f"Correlation coefficient between col 0 and col 1: {corr_col:.4f}")

    def demo_indexing(self):
        if self.matrix is None:
            print("No matrix.")
            return

        print("\n=== NumPy Indexing and Slicing Demo ===")
        print(f"Matrix:\n{self.matrix}")

        print(f"Element at (0,0): {self.matrix[0,0]}")
        print(f"First row: {self.matrix[0, :]}")
        print(f"First column: {self.matrix[:, 0]}")
        # rows 0..n/2, columns 0..m/2
        half_n = self.n // 2
        half_m = self.m // 2
        if half_n > 0 and half_m > 0:
            submatrix = self.matrix[:half_n, :half_m]
            print(f"Submatrix (top-left {half_n}x{half_m}):\n{submatrix}")

        mask = self.matrix > 50
        print(f"Boolean mask (element > 50):\n{mask}")
        print(f"Elements > 50: {self.matrix[mask]}")

        self.matrix[0, 0] = 999
        print(f"After setting (0,0) to 999:\n{self.matrix}")
        self.generate_matrix()  

    @staticmethod
    def demo_array_creation():
        """Static method to show various NumPy array creation functions."""
        print("\n=== Array creation functions ===")
        a = np.array([1, 2, 3])                     
        print(f"np.array([1,2,3]) -> {a}")
        z = np.zeros((2, 3))                        
        print(f"np.zeros((2,3)):\n{z}")
        o = np.ones((2, 3))                         
        print(f"np.ones((2,3)):\n{o}")
        f = np.full((2, 3), 7)                      
        print(f"np.full((2,3),7):\n{f}")
        r = np.arange(0, 10, 2)                    
        print(f"np.arange(0,10,2) -> {r}")
        l = np.linspace(0, 1, 5)                   
        print(f"np.linspace(0,1,5) -> {l}")