from unittest import TestCase, main
from ATM_program import verify_pin, log_in

class TestVerificationPin(TestCase):

    def test_pin_(self):
        expected = True
        result = verify_pin('1234')
        self.assertEqual(expected, result)


    def test_not_pin(self):
        expected = False
        result = verify_pin('8546')
        self.assertEqual(expected, result)

class TestLogIn(TestCase):
    def test_log_in(self):
        expected = True
        result = log_in()
        self.assertTrue(expected, result)

    # class test_Atm_Withdrawal(TestCase)

























if __name__ == '__main__':
    main()

