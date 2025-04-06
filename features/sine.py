import numpy as np
from .base import Function


class SineFunction(Function):
    """Sine function class."""

    @property
    def name(self) -> str:
        return "Sine Wave"

    @property
    def param_a_desc(self) -> str:
        return "Amplitude"

    @property
    def param_b_desc(self) -> str:
        return "Frequency"

    def calculate(self, x: float, a: float, b: float) -> float:
        """Calculates the y value for the Sine function, f(x) = A * sin(B * x)."""
        return a * np.sin(b * x)
