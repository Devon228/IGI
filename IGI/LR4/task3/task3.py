'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: task3
Implements Task3 for series analysis of ln(1-x).
Includes statistical calculations and plotting with matplotlib.
'''

import os
import matplotlib.pyplot as plt
from common.task import Task
from common.action import Action
from common.ui import read_float, show_table
from .series_analyzer import SeriesAnalyzer
from .statistics_mixin import StatisticsMixin


class Task3(Task, StatisticsMixin):
    """
    Task 3: Series expansion of ln(1-x), statistics, and plotting.
    Inherits from Task (menu system) and StatisticsMixin (statistical functions).
    """
    name = "Task 3: Series Analysis of ln(1-x)"

    def __init__(self):
        self.analyzer = None  
        self._data_list = []   # list of partial sums
        self._update_data_list()

    def _update_data_list(self):
        """Update the internal list of partial sums for statistics."""
        if self.analyzer:
            self._data_list = self.analyzer.partial_sums
        else:
            self._data_list = []

    def menu_text(self) -> str:
        if self.analyzer:
            return (f"Series: ln(1-{self.analyzer.x:.4f})\n"
                    f"Precision: {self.analyzer.eps:.2e}\n"
                    f"Terms computed: {len(self.analyzer)}")
        else:
            return "Series Analysis of ln(1-x)\nNo parameters set. Please input x and eps."

    def actions(self):
        return super().actions() + [
            Action("Set x and epsilon", self.set_parameters),
            Action("Show convergence table", self.show_table),
            Action("Show statistics (partial sums)", self.show_statistics),
            Action("Plot convergence graph", self.plot_graph),
            Action("Save graph to file", self.save_graph)
        ]

    def set_parameters(self):
        """Prompt user for x (|x|<1) and epsilon (>0)."""
        x = read_float("Enter x (|x| < 1): ", min=-0.999999, max=0.999999)
        eps = read_float("Enter epsilon (precision): ", min=1e-12, max=0.1)
        self.analyzer = SeriesAnalyzer(x, eps)
        self._update_data_list()
        print(f"Parameters set. Computed {len(self.analyzer)} terms to reach precision.")

    def show_table(self):
        if not self.analyzer:
            print("No data. Set parameters first.")
            return
        rows = []
        for n, partial, exact, error in self.analyzer.data:
            rows.append((self.analyzer.x, n, partial, exact, error))
        headers = ["x", "n", "F(x)", "math_ln(1-x)", "error"]
        show_table(rows, headers)

    def show_statistics(self):
        if not self.analyzer:
            print("No data. Set parameters first.")
            return
        print("\n=== Statistics of partial sums (F(x)) ===")
        print(f"Mean: {self.mean():.8f}")
        print(f"Median: {self.median():.8f}")
        mode_val = self.mode()
        print(f"Mode: {mode_val}")
        print(f"Variance (sample): {self.variance(sample=True):.8f}")
        print(f"Standard deviation (sample): {self.std_dev(sample=True):.8f}")

    def _plot(self, save_filename: str = None):
        """
        Internal plotting function. If save_filename is given, saves to file.
        Otherwise displays the plot.
        """
        if not self.analyzer:
            print("No data. Set parameters first.")
            return

        n_vals = [row[0] for row in self.analyzer.data]
        partial_vals = [row[1] for row in self.analyzer.data]
        exact_val = self.analyzer.exact_value

        plt.figure(figsize=(10, 6))
        plt.plot(n_vals, partial_vals, 'o-', color='blue', label='Series partial sum F(x)', markersize=4)
        # exact value as horizontal line
        plt.axhline(y=exact_val, color='red', linestyle='--', label=f'math.ln(1-x) = {exact_val:.6f}')

        # Annotation: point where precision reached
        last_n = n_vals[-1]
        last_partial = partial_vals[-1]
        plt.annotate(f'Reached eps at n={last_n}',
                     xy=(last_n, last_partial),
                     xytext=(last_n - len(n_vals)*0.1, last_partial + 0.01),
                     arrowprops=dict(facecolor='black', shrink=0.05),
                     fontsize=9)

        # Labels, legend, grid
        plt.xlabel('Number of terms (n)')
        plt.ylabel('Function value')
        plt.title(f'Convergence of ln(1-{self.analyzer.x:.4f}) series (eps={self.analyzer.eps:.2e})')
        plt.legend()
        plt.grid(True, linestyle=':', alpha=0.7)

        if save_filename:
            plt.savefig(save_filename, dpi=150, bbox_inches='tight')
            print(f"Graph saved to {save_filename}")
        else:
            plt.show()
        plt.close()

    def plot_graph(self):
        """Display the graph interactively."""
        self._plot()

    def save_graph(self):
        """Save graph to a PNG file."""
        if not self.analyzer:
            print("No data. Set parameters first.")
            return
        os.makedirs("results", exist_ok=True)
        filename = f"results/ln_series_{self.analyzer.x}_{self.analyzer.eps}.png"
        filename = filename.replace('.', '_').replace('-', 'm')
        self._plot(save_filename=filename)