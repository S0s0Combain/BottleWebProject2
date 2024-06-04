import unittest
import re
import reviews_handler

class TestValidationFunctions(unittest.TestCase):
    
    def test_is_valid_name(self):
        # Test valid name
        valid_name = "Dinae"
        self.assertTrue(reviews_handler.is_valid_name(valid_name)[0], "Expected valid name to pass validation.")
        
        # Test name with special characters
        invalid_name = "Dinar!123"
        self.assertFalse(reviews_handler.is_valid_name(invalid_name)[0], "Expected name with special characters to fail validation.")
        
        # Test name length less than 2
        short_name = "A"
        self.assertFalse(reviews_handler.is_valid_name(short_name)[0], "Expected name with length less than 2 to fail validation.")
        
        # Test name length more than 50
        long_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ut lectus."
        self.assertFalse(reviews_handler.is_valid_name(long_name)[0], "Expected name with length more than 50 to fail validation.")

    def test_is_valid_phone(self):
        # Test valid phone numbers
        valid_phone_1 = "+71234567890"
        valid_phone_2 = "81234567890"
        self.assertTrue(reviews_handler.is_valid_phone(valid_phone_1)[0], "Expected valid phone number to pass validation.")
        self.assertTrue(reviews_handler.is_valid_phone(valid_phone_2)[0], "Expected valid phone number to pass validation.")
        
        # Test invalid phone numbers
        invalid_phone_1 = "+7(123)456-78-90"
        invalid_phone_2 = "1234567890"
        invalid_phone_3 = "812345678901"
        self.assertFalse(reviews_handler.is_valid_phone(invalid_phone_1)[0], "Expected invalid phone number to fail validation.")
        self.assertFalse(reviews_handler.is_valid_phone(invalid_phone_2)[0], "Expected invalid phone number to fail validation.")
        self.assertFalse(reviews_handler.is_valid_phone(invalid_phone_3)[0], "Expected invalid phone number to fail validation.")
        
if __name__ == '__main__':
    unittest.main()
