import unittest
from day_1 import calibrate_line, calibration_sum, convert_to_digits
class TestDay1(unittest.TestCase):
    def test_calibrate_line_should_return_correct_value(self):
        line = "1abc2"
        result = calibrate_line(line)
        self.assertEqual(result, 12)

        line2 = "eightwothree"
        result2 = calibrate_line(line2)
        self.assertEqual(result2, 83)

        line3 = "twoneighthree"
        result3 = calibrate_line(line3)
        self.assertEqual(result3, 23)


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

        inputPt2 = """ \
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen\
        """
        result = calibration_sum(inputPt2)
        self.assertEqual(result, 281)

    def test_convert_to_digits(self):
        line = "eightwothree"
        result = convert_to_digits(line)
        self.assertEqual(result, "8wo3")

