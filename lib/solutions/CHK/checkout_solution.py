from typing import Dict, Tuple

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus: str) -> int:
        
        prices: Dict[str, int] = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15
        }

        offers: Dict[str, Tuple[int, int]] = {
            "A": [3, 130],
            "B": [2, 45]
        }

        return -1



