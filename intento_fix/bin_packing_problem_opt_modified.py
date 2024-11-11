
from typing import Generator
from aima.search import Problem
from bin_packing_operators_modified import AzamonOperator
from bin_packing_state_opt_modified import StateRepresentation

class AzamonProblem(Problem):
    def __init__(self, initial_state: StateRepresentation, maximize_happiness: bool = False, use_entropy=False, mode_simulated_annealing: bool = False, combine_heuristic: bool = False, alpha: float = 0.1):
        self.maximize_happiness = maximize_happiness
        self.use_entropy = use_entropy
        self.mode_simulated_annealing = mode_simulated_annealing
        self.combine_heuristic = combine_heuristic
        self.alpha = alpha
        super().__init__(initial_state)

    def actions(self, state: StateRepresentation) -> Generator[AzamonOperator, None, None]:
        return state.generate_actions(self.mode_simulated_annealing)

    def result(self, state: StateRepresentation, action: AzamonOperator) -> StateRepresentation:
        return state.apply_action(action)

    def value(self, state: StateRepresentation) -> float:

        # Heurística combinada con ponderaciones
        if self.maximize_happiness:
            return state.heuristic_happiness()  # Maximizar solo la felicidad
        elif self.combine_heuristic:
            return -((1-self.alpha)*state.heuristic_cost() - (self.alpha*state.heuristic_happiness2()))
        else:
            return -state.heuristic_cost() # Minimizar solo el coste

    def goal_test(self, state: StateRepresentation) -> bool:
        return False
        #return state.is_goal()