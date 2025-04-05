from abc import ABC, abstractmethod


class Function(ABC):
    """Abstract base class for all functions that are inherited by all feature functions.

    Args:
        ABC (_type_): _description_

    Returns:
        _type_: _description_
    """

    @abstractmethod
    def name(self) -> str:
        """Returns the name of the function.

        Returns:
            str: _description_
        """
        pass

    @abstractmethod
    def param_a_desc(self) -> str:
        """Returns the description of parameter A.

        Returns:
            str: _description_
        """
        pass

    @abstractmethod
    def param_b_desc(self) -> str:
        """Returns the description of parameter B.

        Returns:
            str: _description_
        """
        pass

    @abstractmethod
    def default_param_a(self) -> float:
        """Returns the default value of parameter A.

        Returns:
            float: _description_
        """
        pass

    @abstractmethod
    def default_param_b(self) -> float:
        """Returns the default value of parameter B.

        Returns:
            float: _description_
        """
        pass

    @abstractmethod
    def calculate(self, x: float, a: float, b: float) -> float:
        """Calculates the y value for the selected function for given x, A, and B.

        Args:
            x (float): x value
            a (float): parameter A
            b (float): parameter B

        Returns:
            float: y value
        """
        pass
