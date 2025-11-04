import pytest
from lib.solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_sum_when_param_is_out_of_bounds(self):
        with pytest.raises(ValueError, match="Both numbers should be between 0 and 100 inclusive"):
            SumSolution().compute(150, 10)

        with pytest.raises(ValueError, match="Both numbers should be between 0 and 100 inclusive"):
            SumSolution().compute(4, -10)
