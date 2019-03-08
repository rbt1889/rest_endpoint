import unittest
from rest_endpoint import sum_of_list 

class SumTestCase(unittest.TestCase): 
    """Tests for 'rest_endpoint.py'."""
    
    def test_app_list(self):
        """Test generating the sum of the list hardcoded in rest_endpoint.py"""
        test_total = sum_of_list(list(range(10000001)))
        self.assertEqual(test_total, 50000005000000)

    def test_zero_range(self):
        """Test generating the sum of zero range"""
        test_total = sum_of_list(list(range(0)))
        self.assertEqual(test_total, 0)
    
    def test_big_range(self):
        """Test generating the sum of a list bigger than 10000001 in length"""
        test_total = sum_of_list(list(range(100000002)))
        self.assertEqual(test_total, "Your list is too big")
    
    def test_non_int(self):
        """Test generating the sum of a list with non-int members in it"""
        test_total = sum_of_list([5, 6, 10, 10000001, '4', 'a'])
        self.assertEqual(test_total, "Your list should contain only numbers")
    
    def test_negative_int(self):
        """Test generating the sum of a list with non-int members in it"""
        test_total = sum_of_list([-5, -6, -10, -10000001, -4, -999999999999999999])
        self.assertEqual(test_total, -1000000000010000025)

    def test_mixed_numbers(self):
        """Test generating the sum of a list with mixed number types"""
        test_total = sum_of_list([5.5, -6.0454, 10, -10000001, -4, 0, -3.014, 10001])
        self.assertEqual(test_total, -9989997.5594)
        
unittest.main()