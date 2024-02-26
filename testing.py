import unittest
import sys
sys.path.append('C:\\Users\\admin\\Desktop\\creditcard_validation')
from cc_validationpython import cc_validation

class TestCCValidation(unittest.TestCase):

    def test_valid_credit_card(self):
        # Test valid credit card numbers
        valid_credit_cards = ["4556737586899855", "4532260974760265"]
        for card_number in valid_credit_cards:
            self.assertTrue(cc_validation(card_number), f"{card_number} should be valid")

    def test_invalid_credit_card(self):
        # Test invalid credit card numbers
        invalid_credit_cards = ["1234567890123456", "9876543210987654", "1111222233334444"]
        for card_number in invalid_credit_cards:
            self.assertTrue(cc_validation(card_number), f"{card_number} should be invalid")

    def test_empty_string(self):
        # Test empty string
        self.assertFalse(cc_validation(""), "Empty string should be invalid")

    def test_non_numeric_input(self):
    # Test non-numeric input
        non_numeric_input = ["abcd1234efgh5678", "!@#$%^&*()"]
        for card_number in non_numeric_input:
            try:
                cc_validation(card_number)
                self.fail("Expected ValueError but no exception was raised")
            except ValueError:
                pass  


if __name__ == '__main__':
    unittest.main()
