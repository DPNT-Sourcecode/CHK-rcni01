from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_correct_return_for_incorrect_type(self):
        assert CheckoutSolution().checkout(123) == -1

    def test_correct_return_for_incorrect_letters(self):
        assert CheckoutSolution().checkout("TGH") == -1
        assert CheckoutSolution().checkout("AABCDF") == -1

    def test_correct_return_for_sku_A(self):
        assert CheckoutSolution().checkout("A") == 50

    def test_correct_return_for_sku_AAA(self):
        assert CheckoutSolution().checkout("AAA") == 130