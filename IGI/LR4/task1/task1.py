'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: forest_task
Implements the menu-driven user interface for the Forest monitoring program.
Inherits from common.Task and uses common.Action and common.ui helpers.
'''

from common.task import Task
from common.action import Action
from common.ui import read_int, read_str, show_table
from .forest import Forest
from .tree_species import TreeSpecies

class Task1(Task):
    """
    Main task for the Forest lab.
    Provides menu options: add species, show species info, summary, CSV/Pickle save/load.
    """

    name = "Task 1: Forest Monitoring"

    def __init__(self):
        """Initialize an empty forest."""
        self.forest = Forest()

    def menu_text(self) -> str:
        """
        Return the text displayed at the top of the menu.
        Shows current forest statistics.

        Returns:
            str: Formatted statistics summary.
        """
        total = self.forest.total_trees()
        healthy = self.forest.total_healthy_trees()
        sick_percent = self.forest.overall_sick_percentage()
        return (f"=== Forest Status ===\n"
                f"Total trees: {total}\n"
                f"Healthy trees: {healthy}\n"
                f"Sick trees: {total - healthy}\n"
                f"Overall sick percentage: {sick_percent:.2f}%")

    def actions(self) -> list:
        """
        Define available actions for the menu.

        Returns:
            list[Action]: List of Action objects.
        """
        return super().actions() + [
            Action("Add tree species", self.add_species),
            Action("Show species info", self.show_species),
            Action("Show detailed summary", self.show_summary),
            Action("Save to CSV", self.save_csv),
            Action("Load from CSV", self.load_csv),
            Action("Save to Pickle", self.save_pickle),
            Action("Load from Pickle", self.load_pickle),
        ]

    def add_species(self) -> None:
        """Prompt user for species data and add to forest."""
        name = read_str("Species name: ")
        total = read_int("Total number of trees: ", min=0)
        healthy = read_int("Healthy trees: ", min=0, max=total)
        species = TreeSpecies(name, total, healthy)
        self.forest.add_species(species)
        print(f"Added {name}.")

    def show_species(self) -> None:
        """
        Search for a species by name and display its full information:
        total, healthy, sick, sick percentage, and share of total forest.
        """
        name = read_str("Enter species name: ")
        species = self.forest.find_species(name)
        if species is None:
            print("Species not found.")
        else:
            print(f"\nSpecies: {species.name}")
            print(f"Total trees: {species.total_count}")
            print(f"Healthy: {species.healthy_count}")
            print(f"Sick: {species.sick_count}")
            print(f"Sick percentage within species: {species.sick_percentage:.2f}%")
            total_all = self.forest.total_trees()
            if total_all > 0:
                share = (species.total_count / total_all) * 100
                print(f"Share of total forest: {share:.2f}%")

    def show_summary(self) -> None:
        """
        Print a table showing for each species:
        - total count
        - percentage of total forest trees
        - percentage of sick trees within that species
        """
        summary = self.forest.get_species_summary()
        if not summary:
            print("No data.")
            return
        print("\n--- Forest composition ---")
        print(f"{'Species':<15} {'Total':<8} {'% of total':<12} {'% sick in species':<18}")
        print("-" * 55)
        for item in summary:
            print(f"{item['name']:<15} {item['total']:<8} {item['percent_of_total']:>10.2f}% "
                  f"{item['sick_percent_in_species']:>16.2f}%")

    def save_csv(self) -> None:
        """Save forest data to CSV file using forest.save_csv()."""
        self.forest.save_csv()
        print("Saved to forest.csv")

    def load_csv(self) -> None:
        """Load forest data from CSV file using forest.load_csv()."""
        self.forest.load_csv()
        print("Loaded from forest.csv")

    def save_pickle(self) -> None:
        """Save forest data to binary pickle file."""
        self.forest.save_pickle()
        print("Saved to forest.pkl")

    def load_pickle(self) -> None:
        """Load forest data from binary pickle file."""
        self.forest.load_pickle()
        print("Loaded from forest.pkl")