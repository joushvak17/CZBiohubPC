import math
from .base import Function


class SineFunction(Function):
    """Sine function class."""

    def name(self) -> str:
        return "Sine Wave"

    def param_a_desc(self) -> str:
        return "Amplitude"

    def param_b_desc(self) -> str:
        return "Angular Frequency"

    def default_param_a(self) -> float:
        return 1.0

    def default_param_b(self) -> float:
        return 1.0

    def calculate(self, x: float, a: float, b: float) -> float:
        """Calculates the y value for the Sine function, f(x) = A * sin(B * x)."""
        return a * math.sin(b * x)
