'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: task6b
Pandas analysis of Melbourne Housing dataset.
Task: Compare average price for max rooms vs min rooms.
'''

"""
Module: task6a
Demonstrates Pandas Series, DataFrame, and MultiIndex operations
using the Melbourne Housing dataset.
"""

import pandas as pd
from common.task import Task
from common.action import Action


class Task6a(Task):
    name = "Task 6a: Pandas MultiIndex Series (Melbourne Housing)"

    def __init__(self):
        self.df = None         
        self.price_series = None  

    def menu_text(self) -> str:
        if self.df is not None:
            return f"Dataset loaded: {self.df.shape[0]} rows, {self.df.shape[1]} columns"
        else:
            return "No dataset. Please load Melbourne Housing CSV."

    def actions(self):
        return super().actions() + [
            Action("Load Melbourne Housing CSV", self.load_data),
            Action("Show basic DataFrame info", self.show_df_info),
            Action("Create MultiIndex Series (Region, Address -> Price)", self.create_multindex_series),
            Action("Demonstrate .loc and .iloc on Series", self.demo_loc_iloc),
            Action("Show MultiIndex operations", self.demo_multiindex_ops),
        ]

    def load_data(self):
        """Load Melbourne housing dataset from CSV file."""
        path = "/home/dimas/University/sem 4/IGI/LR4/task6/Melbourne_housing.csv"
        if not path:
            path = "LR4/task6/Melbourne_housing.csv"
        try:
            self.df = pd.read_csv(path)
            print(f"Loaded {len(self.df)} records.")
            print("Columns:", list(self.df.columns))
        except FileNotFoundError:
            print("File not found. Please download the dataset from Kaggle.")
        except Exception as e:
            print(f"Error: {e}")

    def show_df_info(self):
        if self.df is None:
            print("No data loaded.")
            return
        print("\n=== DataFrame Info ===")
        print(f"Shape: {self.df.shape}")
        print("\nData types:")
        print(self.df.dtypes)
        print("\nFirst 5 rows:")
        print(self.df.head())
        print("\nStatistical summary (numeric):")
        print(self.df.describe())

    def create_multindex_series(self):
        """
        Create a MultiIndex Series with levels:
        - Level 0: Regionname (or Suburb if Regionname missing)
        - Level 1: Address
        Values: Price
        """
        if self.df is None:
            print("No data loaded.")
            return

        if 'Price' not in self.df.columns:
            print("Column 'Price' not found.")
            return

        level0_col = 'Regionname' if 'Regionname' in self.df.columns else 'Suburb'
        level1_col = 'Address' if 'Address' in self.df.columns else 'Suburb'

        if level0_col not in self.df.columns or level1_col not in self.df.columns:
            print(f"Required columns {level0_col} or {level1_col} missing.")
            return

        temp = self.df.dropna(subset=[level0_col, level1_col, 'Price'])
        if temp.empty:
            print("No valid rows after dropping NA.")
            return

        multi_index = pd.MultiIndex.from_arrays(
            [temp[level0_col], temp[level1_col]],
            names=[level0_col, level1_col]
        )
        self.price_series = pd.Series(temp['Price'].values, index=multi_index)
        print(f"MultiIndex Series created with {len(self.price_series)} entries.")
        print("First 10 entries:")
        print(self.price_series.head(10))

    def demo_loc_iloc(self):
        if self.price_series is None:
            print("No MultiIndex Series. Run 'Create MultiIndex Series' first.")
            return

        print("\n=== Accessing elements using .loc and .iloc ===")

        # 1. Используем .iloc[0] – всегда скаляр
        first_value = self.price_series.iloc[0]
        print(f"First element via .iloc[0]: {first_value:.2f}")

        # 2. .loc по полной метке – осторожно, может вернуть Series при дубликатах
        idx0 = self.price_series.index[0]
        val = self.price_series.loc[idx0]
        if isinstance(val, pd.Series):
            # Если дубликаты, берём первый
            val = val.iloc[0]
        print(f"Value at first index {idx0}: {val:.2f}")

        # 3. Срез по первому уровню (регион) – показываем, как работает .loc
        level0_name = self.price_series.index.names[0]
        unique_level0 = self.price_series.index.get_level_values(0).unique()
        if len(unique_level0) > 0:
            first_region = unique_level0[0]
            region_series = self.price_series.loc[first_region]  # возвращает Series
            print(f"\nFirst 5 prices for region '{first_region}':")
            print(region_series.head())
            print(f"Average price in that region: {region_series.mean():.2f}")

        # 4. .iloc срез первых 5 элементов
        print("\nFirst 5 elements via .iloc[:5]:")
        print(self.price_series.iloc[:5])

    def demo_multiindex_ops(self):
        if self.price_series is None:
            print("No MultiIndex Series. Run 'Create MultiIndex Series' first.")
            return

        print("\n=== MultiIndex operations ===")
        # 1. Получение всех значений для конкретного первого уровня (регион)
        level0_name = self.price_series.index.names[0]
        regions = self.price_series.index.get_level_values(0).unique()
        print(f"Available {level0_name}s (first 5): {list(regions[:5])}")

        if len(regions) > 0:
            sample_region = regions[0]
            print(f"\nAverage price for region '{sample_region}':")
            avg = self.price_series.loc[sample_region].mean()
            print(f"${avg:.2f}")

        # 2. xs (cross-section) – выбор по одному уровню
        if len(regions) > 1:
            second_region = regions[1]
            print(f"\nPrices for region '{second_region}' using xs:")
            xs_data = self.price_series.xs(second_region, level=level0_name)
            print(xs_data.head())

        # 3. Группировка по первому уровню (средняя цена по регионам)
        print("\nAverage price by region (first 5):")
        grouped = self.price_series.groupby(level=0).mean()
        print(grouped.head())

        # 4. Сортировка по значениям
        print("\nTop 5 highest prices:")
        print(self.price_series.nlargest(5))

        # 5. Фильтрация по условию (цена > 2_000_000)
        expensive = self.price_series[self.price_series > 2_000_000]
        print(f"\nNumber of houses with price > 2,000,000: {len(expensive)}")
