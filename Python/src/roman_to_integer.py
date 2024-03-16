class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000,
                 'IV': 4,
                 'IX': 9,
                 'XL': 40,
                 'XC': 90,
                 'CD': 400,
                 'CM': 900}

        result = 0
        i = 0

        while i < len(s) - 1:
            current_char = s[i]
            next_char = s[i + 1]
            if self.is_simple_number(current_char, next_char, roman):
                self.add_to_result(roman, current_char, result)
                i += 1
            else:
                compound = self.create_compound_number(current_char, next_char)
                self.add_to_result(roman, compound, result)
                i += 2

        if i == len(s) - 1:
            current_char = s[i]
            self.add_to_result(roman, current_char, result)

        return result

    def create_compound_number(self, current_char, next_char):
        compound = current_char + next_char
        return compound

    def is_simple_number(self, current_char, next_char, roman):
        return roman.get(current_char) >= roman.get(next_char)

    def add_to_result(self, roman, roman_number, result):
        result += roman.get(roman_number)
