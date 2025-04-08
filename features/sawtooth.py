import numpy as np
from .base import Function


class SawtoothFunction(Function):
    """
    Sawtooth wave function class. 
    - Wavelength of 4 X-units
    - Flat section is 1 X-unit long, y=B
    - Up-slope section is 1 X-unit long
    - Down-slope section is 2 X-units long
    """

    @property
    def name(self) -> str:
        return "Sawtooth Wave"

    @property
    def param_a_desc(self) -> str:
        return "Amplitude"

    @property
    def param_b_desc(self) -> str:
        return "Vertical Position"

    def calculate(self, x: float, a: float, b: float) -> float:
        """Calculates the y value for the Sawtooth function."""

        # Use numpy array on x and y for faster calculations
        x_values = np.asarray(x, dtype=float)
        y_values = np.zeros_like(x_values, dtype=float)

        # Each period is every 4 X-units
        # Use modulo to find the position within the period
        period = np.mod(x_values, 4)

        # The flat section is 1 X-unit long
        # Which is always y=b
        y_values[period < 1] = b

        # The up-slope section is 1 X-unit long
        # Which is y = b + a * (x - 1)
        up_slope = (period >= 1) & (period < 2)
        y_values[up_slope] = b + a * (period[up_slope] - 1)

        # The down-slope section is 2 X-units long
        # Which is y = b + a - (a / 2) * (x - 2)
        down_slope = (period >= 2) & (period < 4)
        y_values[down_slope] = b + a - (a / 2) * (period[down_slope] - 2)

        return y_values
