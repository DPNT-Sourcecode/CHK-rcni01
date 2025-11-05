from typing import Dict, Tuple
from collections import Counter

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

        skuCounts: Counter[str] = Counter(skus)

        total: int = 0
        
        for sku, count in skuCounts.items():
            if sku in offers:
                offerCount, offerPrice = offers[sku]
                

        

        return total
