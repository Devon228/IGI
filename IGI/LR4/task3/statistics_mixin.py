'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: statistics_mixin
Provides a mixin class for statistical calculations on a list of numbers.
'''

from typing import List, Union
from collections import Counter
import math

class StatisticsMixin:
    """
    Mixin that adds statistical methods to a class.
    Requires self._data_list (list of numeric values) to be present.
    """

    def mean(self) -> float:
        """Arithmetic mean of the data."""
        if not self._data_list:
            return 0.0
        return sum(self._data_list) / len(self._data_list)

    def median(self) -> float:
        """Median of the data."""
        n = len(self._data_list)
        if n == 0:
            return 0.0
        sorted_data = sorted(self._data_list)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]

    def mode(self) -> Union[float, List[float]]:
        """
        Mode(s) of the data. Returns a single value if unique mode,
        otherwise a list of values (multimodal).
        """
        if not self._data_list:
            return 0.0
        counter = Counter(self._data_list)
        max_freq = max(counter.values())
        modes = [val for val, freq in counter.items() if freq == max_freq]
        return modes[0] if len(modes) == 1 else modes

    def variance(self, sample: bool = True) -> float:
        """
        Variance of the data.
        If sample=True (default), computes sample variance (divided by n-1).
        If sample=False, computes population variance (divided by n).
        """
        n = len(self._data_list)
        if n == 0:
            return 0.0
        mean_val = self.mean()
        sq_dev = sum((x - mean_val) ** 2 for x in self._data_list)
        if sample:
            return sq_dev / (n - 1) if n > 1 else 0.0
        else:
            return sq_dev / n

    def std_dev(self, sample: bool = True) -> float:
        """Standard deviation (sqrt of variance)."""
        return math.sqrt(self.variance(sample))