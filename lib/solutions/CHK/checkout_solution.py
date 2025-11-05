from typing import Dict, Tuple
from collections import Counter
import math

class CheckoutSolution:

    # CHK_R2 answer
    def checkout(self, skus) -> int:
        if type(skus) != str:
            return -1
        
        prices: Dict[str, int] = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40
        }

        for sku in skus:
            if sku not in prices:
                return -1

        skuCounts: Counter[str] = Counter(skus)

        total: int = 0

        if "A" in skuCounts:
            f

        return total
