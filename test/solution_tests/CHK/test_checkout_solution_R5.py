from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_correct_return_for_incorrect_type(self):
        assert CheckoutSolution().checkout(123) == -1

    def test_correct_return_for_incorrect_letters(self):
        assert CheckoutSolution().checkout("TG+H") == -1
        assert CheckoutSolution().checkout("AAB2CDFG") == -1

    def test_correct_return_for_sku_AAAAAAAA(self):
        assert CheckoutSolution().checkout("AAAAAAAA") == 330
    
    def test_correct_return_for_sku_STXYZ(self):
        assert CheckoutSolution().checkout("STXYZ") == 82