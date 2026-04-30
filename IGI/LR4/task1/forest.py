'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: forest
Manages a collection of tree species and provides statistical calculations.
Supports CSV and Pickle serialization.
'''

import csv
import pickle
from typing import List, Optional, Dict, Any
from .tree_species import TreeSpecies

class Forest:
    """
    Container for multiple TreeSpecies objects.
    Computes aggregated forest statistics.
    """

    def __init__(self):
        """Initialize an empty forest (no species)."""
        self._species_list: List[TreeSpecies] = []

    def add_species(self, species: TreeSpecies) -> None:
        """
        Add a tree species to the forest.

        Args:
            species (TreeSpecies): Species object to add.
        """
        self._species_list.append(species)

    def find_species(self, name: str) -> Optional[TreeSpecies]:
        """
        Find a species by name (case-insensitive).

        Args:
            name (str): Species name to search for.

        Returns:
            Optional[TreeSpecies]: Species object if found, else None.
        """
        return next((s for s in self._species_list if s.name.lower() == name.lower()), None)

    def total_trees(self) -> int:
        """
        Calculate total number of trees across all species.

        Returns:
            int: Sum of total_count for all species.
        """
        return sum(s.total_count for s in self._species_list)

    def total_healthy_trees(self) -> int:
        """
        Calculate total number of healthy trees across all species.

        Returns:
            int: Sum of healthy_count for all species.
        """
        return sum(s.healthy_count for s in self._species_list)

    def overall_sick_percentage(self) -> float:
        """
        Calculate overall percentage of sick trees in the whole forest.

        Returns:
            float: Sick percentage (0-100). Returns 0 if no trees.
        """
        total = self.total_trees()
        if total == 0:
            return 0.0
        healthy_total = self.total_healthy_trees()
        return ((total - healthy_total) / total) * 100

    def get_species_summary(self) -> List[Dict[str, Any]]:
        """
        Generate a summary for each species: name, total count,
        percentage of total forest trees, and sick percentage within species.

        Returns:
            List[Dict]: List of dictionaries with keys:
                'name', 'total', 'percent_of_total', 'sick_percent_in_species'
        """
        grand_total = self.total_trees()
        result = []
        for s in self._species_list:
            percent_of_total = (s.total_count / grand_total * 100) if grand_total > 0 else 0
            result.append({
                'name': s.name,
                'total': s.total_count,
                'percent_of_total': percent_of_total,
                'sick_percent_in_species': s.sick_percentage
            })
        return result

    def save_csv(self, filename: str = "forest.csv") -> None:
        """
        Save forest data to a CSV file.

        Args:
            filename (str): Output file name. Default 'forest.csv'.

        Format: header row "Species,TotalCount,HealthyCount", then one row per species.
        """
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Species", "TotalCount", "HealthyCount"])
            for s in self._species_list:
                writer.writerow([s.name, s.total_count, s.healthy_count])

    def load_csv(self, filename: str = "forest.csv") -> None:
        """
        Load forest data from a CSV file (replaces current data).

        Args:
            filename (str): Input file name.

        Raises:
            FileNotFoundError: If file does not exist.
            ValueError: If data format is invalid.
        """
        self._species_list.clear()
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                name, total, healthy = row[0], int(row[1]), int(row[2])
                self.add_species(TreeSpecies(name, total, healthy))

    def save_pickle(self, filename: str = "forest.pkl") -> None:
        """
        Save forest data to a binary pickle file.

        Args:
            filename (str): Output file name. Default 'forest.pkl'.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self._species_list, f)

    def load_pickle(self, filename: str = "forest.pkl") -> None:
        """
        Load forest data from a binary pickle file (replaces current data).

        Args:
            filename (str): Input file name.

        Raises:
            FileNotFoundError: If file does not exist.
            pickle.UnpicklingError: If file is corrupted.
        """
        with open(filename, 'rb') as f:
            self._species_list = pickle.load(f)