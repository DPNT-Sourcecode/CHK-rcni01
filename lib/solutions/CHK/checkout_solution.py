from typing import Dict, Tuple

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus) -> int:
        if type(skus) != str:
            return -1
        
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

        for sku in skus:
            if sku not in prices:
                return -1

        

        return 0




