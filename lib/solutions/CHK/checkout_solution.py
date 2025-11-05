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
            countA = skuCounts["A"]
            firstOfferGroups: int = math.floor(countA / 5)
            total = total + firstOfferGroups * 200
            remainder: int = countA - firstOfferGroups * 5
            if remainder >= 3:
                total = total + 130
                remainder = remainder - 3
            total = total + remainder * 50                
        
        if "E" in skuCounts and "B" in skuCounts:
            countE = skuCounts["E"]
            freeB = 

        if "B" in skuCounts:
            countB = skuCounts["B"]
            offerGroups: int = math.floor(countB / 2)
            remainder: int = countB - offerGroups * 2
            total = total + offerGroups * 45 + remainder * 30


        return total


