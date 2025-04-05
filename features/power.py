import numpy as np
from .base import Function


class PowerFunction(Function):
    """Power function class."""

    @property
    def name(self) -> str:
        return "Power Function"

    @property
    def param_a_desc(self) -> str:
        return "Coefficient"

    @property
    def param_b_desc(self) -> str:
        return "Exponent"

    def calculate(self, x: float, a: float, b: float) -> float:
        """Calculates the y value for the Power function, f(x) = A * x^B."""
        return a * np.power(x, b)
