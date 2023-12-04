import unittest
from day_1 import calibrate_line, calibration_sum
class TestDay1Pt1(unittest.TestCase):
    def test_calibrate_line_should_return_correct_value(self):
        line = "1abc2"
        result = calibrate_line(line)
        self.assertEqual(result, 12)

    def test_calibrate_line_with_1_digit_should_return_correct_value(self):
        line = "treb7uchet"
        result = calibrate_line(line)
        self.assertEqual(result, 77)

    def test_calibration_sum_should_return_correct_value(self):
        input = """\
        1abc2
        ghijpqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet\
        """
        result = calibration_sum(input)
        self.assertEqual(result, 142)
