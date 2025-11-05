from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_correct_return_for_incorrect_type(self):
        assert CheckoutSolution().checkout(123) == -1

    def test_correct_return_for_incorrect_letters(self):
        assert CheckoutSolution().checkout("TGH") == -1
        assert CheckoutSolution().checkout("AABCDF") == -1

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