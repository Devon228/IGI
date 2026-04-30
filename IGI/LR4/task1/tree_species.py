'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: tree_species
Defines the TreeSpecies class representing a tree species in the forest.
'''

class TreeSpecies:
    """
    Represents a tree species with total count and healthy count.
    Provides computed property for sick count and percentage.
    """

    def __init__(self, name: str, total_count: int, healthy_count: int):
        """
        Initialize a tree species.

        Args:
            name (str): Species name (e.g., "Oak", "Pine").
            total_count (int): Total number of trees of this species.
            healthy_count (int): Number of healthy trees.
        """
        self.name = name
        self._total_count = total_count
        self._healthy_count = healthy_count

    @property
    def total_count(self) -> int:
        """Get total number of trees."""
        return self._total_count

    @total_count.setter
    def total_count(self, value: int) -> None:
        """
        Set total number of trees with validation.

        Args:
            value (int): New total count.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("Total count cannot be negative")
        self._total_count = value

    @property
    def healthy_count(self) -> int:
        """Get number of healthy trees."""
        return self._healthy_count

    @healthy_count.setter
    def healthy_count(self, value: int) -> None:
        """
        Set healthy count with validation.

        Args:
            value (int): New healthy count.

        Raises:
            ValueError: If value is negative or exceeds total count.
        """
        if value < 0 or value > self.total_count:
            raise ValueError(f"Healthy count must be between 0 and {self.total_count}")
        self._healthy_count = value

    @property
    def sick_count(self) -> int:
        """
        Compute number of sick trees (total - healthy).

        Returns:
            int: Number of sick trees.
        """
        return self.total_count - self.healthy_count

    @property
    def sick_percentage(self) -> float:
        """
        Compute percentage of sick trees within this species.

        Returns:
            float: Sick percentage (0-100). Returns 0 if total count is 0.
        """
        if self.total_count == 0:
            return 0.0
        return (self.sick_count / self.total_count) * 100

    def __repr__(self) -> str:
        """Return a string representation for debugging."""
        return f"TreeSpecies({self.name}, total={self.total_count}, healthy={self.healthy_count})"