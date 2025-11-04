
class SumSolution:
    
    def compute(self, x: int, y: int) -> int:

        # Both parameters should be between 0 and 100, if not raise a value error
        if not (0 <= x <= 100 and 0 <= y <= 100):
            raise ValueError("Both numbers should be between 0 and 100 inclusive")

        return x + y

