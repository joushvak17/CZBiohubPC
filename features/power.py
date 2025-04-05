import math
from .base import Function


class PowerFunction(Function):
    """Power function class."""

    def name(self) -> str:
        return "Power Function"

    def param_a_desc(self) -> str:
        return "Coefficient"

    def param_b_desc(self) -> str:
        return "Exponent"

    def default_param_a(self) -> float:
        return 1.0

    def default_param_b(self) -> float:
        return 2.0

    def calculate(self, x: float, a: float, b: float) -> float:
        """Calculates the y value for the Power function, f(x) = A * x^B."""
        return a * math.pow(x, b)
