from typing import Dict, Tuple, List
from collections import Counter
import math

PRICES: Dict[str, int] = {
    "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
    "G": 20, "H": 10, "I": 35, "J": 60, "K": 70, "L": 90,
    "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
    "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17,
    "Y": 20, "Z": 21
}

# Buy multiple get another item free offer: number is how much you need to buy to get the nested item free.
FREE_OTHER_ITEM: Dict[str, Tuple[int, str]] = {
    "E": (2, "B"),
    "N": (3, "M"),
    "R": (3, "Q")
}

# Buy multiple get one free offer : number reflects the size required to get a free item. e.g. you need 3 F to get one of them free
FREE_SAME_ITEM: Dict[str, int] = {
    "F": 3,
    "U": 4 
}

# MultiBuy offers : have ordered the offers, so the better offer comes first. Important for later.
MULTIBUY_OFFERS: Dict[str, Tuple[Tuple[int,int], ...]] = {
    "A": ((5, 200), (3, 130)),
    "B": ((2, 45),),
    "H": ((10, 80), (5, 45)),
    "K": ((2, 120),),
    "P": ((5, 200),),
    "Q": ((3, 80),),
    "V": ((3, 130), (2, 90))
}

GROUP_OFFER_ITEMS: List[str] = ["S", "T", "X", "Y", "Z"]
GROUP_OFFER_PRICE: int = 45
GROUP_OFFER_SIZE: int = 3

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
                total = total + PRICES[item] * (groups * (groupSize - 1) + remainder)
                counts[item] = 0
        return total
    
    def applyMultiBuyOffers(self, counts: Counter[str]) -> int:
        total = 0
        for item, offers in MULTIBUY_OFFERS.items():
            if item in counts:
                count: int = counts[item]
                for qty, offerPrice in offers:
                    offerGroups: int = math.floor(count / qty)
                    total = total + offerGroups * offerPrice
                    count = count - offerGroups * qty
                total = total + count * PRICES[item]
                counts[item] = 0
        return total

    def applyGroupOffer(self, counts: Counter[str]) -> int:
        total = 0
        boughtItemsInOffer = []

        for item in GROUP_OFFER_ITEMS:
            boughtItemsInOffer.extend([PRICES[item]] * counts[item])
        
        boughtItemsInOffer.sort()

        while len(boughtItemsInOffer) >= GROUP_OFFER_SIZE:
            total = total + GROUP_OFFER_PRICE

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
        total = total + self.applyFreeSameItemOffers(skuCounts)
        total = total + self.applyMultiBuyOffers(skuCounts)

        for sku, count in skuCounts.items():
            total = total + count * PRICES[sku]

        return total
