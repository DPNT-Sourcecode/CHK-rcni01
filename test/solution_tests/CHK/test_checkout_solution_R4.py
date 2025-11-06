from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_correct_return_for_incorrect_type(self):
        assert CheckoutSolution().checkout(123) == -1

    def test_correct_return_for_incorrect_letters(self):
        assert CheckoutSolution().checkout("T2GH") == -1
        assert CheckoutSolution().checkout("AAB-CDFG") == -1

    def test_correct_return_for_sku_AAAAAAAA(self):
        assert CheckoutSolution().checkout("AAAAAAAA") == 330
    
    def test_correct_return_for_sku_AAAAAAAAAA(self):
        assert CheckoutSolution().checkout("AAAAAAAAAA") == 400
    
    def test_correct_return_for_sku_AAAAAAAAA(self):
        assert CheckoutSolution().checkout("AAAAAAAAA") == 380
    
    def test_correct_return_for_sku_AAAA(self):
        assert CheckoutSolution().checkout("AAAA") == 180

    def test_correct_return_for_sku_BBB(self):
        assert CheckoutSolution().checkout("BBB") == 75

    def test_correct_return_for_sku_BBBBB(self):
        assert CheckoutSolution().checkout("BBBBB") == 120

    def test_correct_return_for_sku_BAABBABAA(self):
        assert CheckoutSolution().checkout("BAABBABAA") == 290

    def test_correct_return_for_sku_EEB(self):
        assert CheckoutSolution().checkout("EEB") == 80
    
    def test_correct_return_for_sku_EEEEB(self):
        assert CheckoutSolution().checkout("EEEEB") == 160
    
    def test_correct_return_for_sku_ABCDE(self):
        assert CheckoutSolution().checkout("ABCDE") == 155   
    
    def test_correct_return_for_sku_AAAAAEEBB(self):
        assert CheckoutSolution().checkout("AAAAAEEBB") == 310

    def test_correct_return_for_sku_FF(self):
        assert CheckoutSolution().checkout("FF") == 20   

    def test_correct_return_for_sku_FFF(self):
        assert CheckoutSolution().checkout("FFF") == 20 

    def test_correct_return_for_sku_FFFF(self):
        assert CheckoutSolution().checkout("FFFF") == 30 

    def test_correct_return_for_sku_FFFFF(self):
        assert CheckoutSolution().checkout("FFFFF") == 40
    
    def test_correct_return_for_sku_FFFFFF(self):
        assert CheckoutSolution().checkout("FFFFFF") == 40

    def test_correct_return_for_sku_FFFFFF(self):
        assert CheckoutSolution().checkout("FFFFFF") == 40

    def test_correct_return_for_sku_NNNM(self):
        assert CheckoutSolution().checkout("NNNM") == 120

    def test_correct_return_for_sku_NNNMM(self):
        assert CheckoutSolution().checkout("NNNMM") == 135

    def test_correct_return_for_sku_RRRQ(self):
        assert CheckoutSolution().checkout("RRRQ") == 150

    def test_correct_return_for_sku_RRRQQ(self):
        assert CheckoutSolution().checkout("RRRQQ") == 180

    def test_correct_return_for_sku_UUUU(self):
        assert CheckoutSolution().checkout("UUUU") == 120

    def test_correct_return_for_sku_UUUUUU(self):
        assert CheckoutSolution().checkout("UUUUUU") == 200

    def test_correct_return_for_sku_VV(self):
        assert CheckoutSolution().checkout("VV") == 90

    def test_correct_return_for_sku_VVV(self):
        assert CheckoutSolution().checkout("VVV") == 130

    def test_correct_return_for_sku_VVVV(self):
        assert CheckoutSolution().checkout("VVVV") == 180

    def test_correct_return_for_sku_HHHHH(self):
        assert CheckoutSolution().checkout("HHHHH") == 45

    def test_correct_return_for_sku_HHHHHHHHHH(self):
        assert CheckoutSolution().checkout("HHHHHHHHHH") == 80

    def test_correct_return_for_sku_KK(self):
        assert CheckoutSolution().checkout("KK") == 150

    def test_correct_return_for_sku_PPPPP(self):
        assert CheckoutSolution().checkout("PPPPP") == 200

    def test_correct_return_for_sku_QQQ(self):
        assert CheckoutSolution().checkout("QQQ") == 80

    def test_correct_return_for_sku_QQQQ(self):
        assert CheckoutSolution().checkout("QQQQ") == 110

    def test_correct_return_for_sku_EEBB(self):
        assert CheckoutSolution().checkout("EEBB") == 110

    def test_correct_return_for_sku_AAAAAEEBBNNNM(self):
        assert CheckoutSolution().checkout("AAAAAEEBBNNNM") == 430

    def test_correct_return_for_sku_STXYZ(self):
        assert CheckoutSolution().checkout("STXYZ") == 200

    def test_correct_return_for_sku_WWY(self):
        assert CheckoutSolution().checkout("WWY") == 50

    def test_correct_return_for_sku_AAAAAAFFFFFF(self):
        assert CheckoutSolution().checkout("AAAAAAFFFFFF") == 290
