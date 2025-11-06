from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout:

    def test_incorrect_type(self):
        assert CheckoutSolution().checkout(123) == -1

    def test_invalid_letters(self):
        assert CheckoutSolution().checkout("T2GH") == -1
        assert CheckoutSolution().checkout("AAB-CDFG") == -1

    def test_single_items(self):
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15
        assert CheckoutSolution().checkout("E") == 40
        assert CheckoutSolution().checkout("F") == 10
        assert CheckoutSolution().checkout("S") == 20
        assert CheckoutSolution().checkout("X") == 17
        assert CheckoutSolution().checkout("Z") == 21

    def test_multi_price_offers(self):
        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAA") == 250
        assert CheckoutSolution().checkout("BB") == 45
        assert CheckoutSolution().checkout("HHHHH") == 45
        assert CheckoutSolution().checkout("HHHHHHHHHH") == 80
        assert CheckoutSolution().checkout("KK") == 120
        assert CheckoutSolution().checkout("PPPPP") == 200
        assert CheckoutSolution().checkout("QQQ") == 80
        assert CheckoutSolution().checkout("VV") == 90
        assert CheckoutSolution().checkout("VVV") == 130

    def test_free_items(self):
        assert CheckoutSolution().checkout("EEB") == 80
        assert CheckoutSolution().checkout("EEEEB") == 160
        assert CheckoutSolution().checkout("FF") == 20
        assert CheckoutSolution().checkout("FFF") == 20
        assert CheckoutSolution().checkout("NNNM") == 120
        assert CheckoutSolution().checkout("RRRQ") == 150
        assert CheckoutSolution().checkout("UUUU") == 120

    def test_group_discount(self):
        assert CheckoutSolution().checkout("SSS") == 45
        assert CheckoutSolution().checkout("STX") == 45
        assert CheckoutSolution().checkout("SSSTTX") == 90
        assert CheckoutSolution().checkout("SSSTTXYYZ") == 135
        assert CheckoutSolution().checkout("SST") == 45
        assert CheckoutSolution().checkout("SXY") == 45
        assert CheckoutSolution().checkout("SXYZZ") == 82

    def test_mixed_baskets(self):
        assert CheckoutSolution().checkout("ABCDE") == 155
        assert CheckoutSolution().checkout("AAAAAEEBB") == 310
        assert CheckoutSolution().checkout("FFFFF") == 40
        assert CheckoutSolution().checkout("BBBBB") == 120
        assert CheckoutSolution().checkout("BAABBABAA") == 290
        assert CheckoutSolution().checkout("WWY") == 60
        assert CheckoutSolution().checkout("STXZ") == 62 
        assert CheckoutSolution().checkout("SSSTTXYYZZ") == 152

    def test_edge_cases(self):
        assert CheckoutSolution().checkout("") == 0

