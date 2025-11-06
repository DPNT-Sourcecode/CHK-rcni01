from typing import Dict, Tuple
from collections import Counter
import math

PRICES: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
    "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90,
    "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
    "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90,
    "Y": 10, "Z": 50
}

FREE_OTHER_ITEM: Dict[str, Tuple[int, str]] = {
    "E": (2, "B"),
    "N": (3, "M"),
    "R": (3, "Q")
}

# number reflects the size required to get a free item. e.g. you need 3 F to get one of them free
FREE_SAME_ITEM: Dict[str, int] = {
    "F": 3,
    "U": 4 
}

MULTIBUY_OFFERS: Dict[str, Tuple[Tuple[int,int], ...]] = {
    "A": ((5, 200), (3, 130)),
    "B": ((2, 45)),
    "H": ((10, 80), (5, 45)),
    "K": ((2, 150)),
    "P": ((5, 200)),
    "Q": ((3, 80)),
    "V": ((3, 130), (2, 90))
}


class CheckoutSolution:

    def applyFreeOtherItemOffers(self, counts: Counter[str]) -> None:
        for groupedItem, (amountNeeded, freeItem) in FREE_OTHER_ITEM.items():
            if groupedItem in counts and freeItem in counts:
                countGrouped: int = counts[groupedItem]
                freeAmount: int = math.floor(countGrouped / amountNeeded)
                counts[freeItem] = max(0, counts[freeItem] - freeAmount)
    
    def applyFreeSameItemOffers(self, counts: Counter[str]) -> int:
        total = 0
        for item, groupSize in FREE_SAME_ITEM.items():
            if item in counts:
                count: int = counts[item]
                groups: int = math.floor(count / groupSize)
                remainder: int = count - groups * groupSize
                total = total + groups * PRICES[item] * groupSize + remainder * PRICES[item]
        return total

    # CHK_R2 answer
    def checkout(self, skus) -> int:
        if type(skus) != str:
            return -1
        
        for sku in skus:
            if sku not in PRICES:
                return -1

        skuCounts: Counter[str] = Counter(skus)

        total: int = 0

        self.applyFreeOtherItemOffers(skuCounts)

        if "A" in skuCounts:
            countA: int = skuCounts["A"]
            firstOfferGroups: int = math.floor(countA / 5)
            total = total + firstOfferGroups * 200
            remainder: int = countA - firstOfferGroups * 5
            if remainder >= 3:
                total = total + 130
                remainder = remainder - 3
            total = total + remainder * 50                
        
        if "F" in skuCounts:
            countF: int = skuCounts["F"]
            groupsOfF: int = math.floor(countF / 3)
            remainder: int = countF - groupsOfF * 3
            total = total + groupsOfF * 20 + remainder * 10


        if "B" in skuCounts:
            countB: int = skuCounts["B"]
            offerGroups: int = math.floor(countB / 2)
            remainder: int = countB - offerGroups * 2
            total = total + offerGroups * 45 + remainder * 30

        for sku in ["C", "D", "E"]:
            total = total + skuCounts[sku] * PRICES[sku]

        return total

