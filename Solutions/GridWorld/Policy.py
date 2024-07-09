"""
Grid World Policy.
"""

from core.dependency.StateIndex import StateIndex
from core.dependency.Action import Action
from core.dependency.StateSpace import StateSpace
from core.Policy.EquiprobablePolicy import EquiprobablePolicy

class GridWorldEquiprobablePolicy[SI: StateIndex, A: Action](EquiprobablePolicy[SI, A]):
    """Equiprobable Policy for Grid World."""
    
    def __init__(
        self,
        state_space: StateSpace[SI, A]
    ) -> None:
        super().__init__(state_space)
