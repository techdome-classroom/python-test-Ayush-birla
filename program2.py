class Solution(object):
    def romanToInt(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        
        for char in s:
            value = roman_dict[char]
            if value > prev_value:
                result += value - 2 * prev_value  # Subtract twice the previous value for cases like IV, IX, XL, XC, etc.
            else:
                result += value
            prev_value = value
        
        return result
