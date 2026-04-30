'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: series_analyzer
Contains the SeriesAnalyzer class that generates terms for ln(1-x) series
and stores the data for analysis.
'''

import math
from typing import List, Tuple, Generator

class SeriesAnalyzer:
    """
    Analyzes the series expansion of ln(1-x) = -x - x^2/2 - x^3/3 - ...
    """
    MAX_ITER = 500

    def __init__(self, x: float, eps: float):
        """
        Initialize with argument x and precision eps.

        Args:
            x (float): must satisfy |x| < 1.
            eps (float): required precision (positive).
        """
        self._x = x
        self._eps = eps
        self._data: List[Tuple[int, float, float, float, float]] = []
        self._generate_table()

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        if not (-1 < value < 1):
            raise ValueError("x must satisfy |x| < 1")
        self._x = value
        self._generate_table()  

    @property
    def eps(self) -> float:
        return self._eps

    @eps.setter
    def eps(self, value: float):
        if value <= 0:
            raise ValueError("eps must be positive")
        self._eps = value
        self._generate_table()

    @property
    def exact_value(self) -> float:
        """Exact value using math.log."""
        return math.log(1 - self._x)

    @property
    def data(self) -> List[Tuple[int, float, float, float, float]]:
        """Full table data: (n, partial_sum, exact, error)."""
        return self._data

    @property
    def partial_sums(self) -> List[float]:
        """List of partial sums (F(x)) for each n."""
        return [row[1] for row in self._data]

    @staticmethod
    def _term_generator(x: float) -> Generator[float, None, None]:
        """
        Generator yielding successive terms of the series: -x^n/n.
        """
        n = 1
        term = -x
        while n <= SeriesAnalyzer.MAX_ITER:
            yield term
            n += 1
            term = - (x ** n) / n

    def _generate_table(self) -> None:
        """
        Generate the convergence table up to MAX_ITER or until error <= eps.
        Stores each row as (n, partial_sum, exact, error).
        """
        self._data.clear()
        partial = 0.0
        exact = self.exact_value
        for n, term in enumerate(self._term_generator(self._x), start=1):
            partial += term
            error = abs(partial - exact)
            self._data.append((n, partial, exact, error))
            if error <= self._eps:
                break

    def __len__(self) -> int:
        """Number of computed terms."""
        return len(self._data)

    def __getitem__(self, index: int) -> Tuple[int, float, float, float]:
        """Access row by index."""
        return self._data[index]

    def __repr__(self) -> str:
        return f"SeriesAnalyzer(x={self._x}, eps={self._eps}, terms={len(self)})"