class Solution:
    def romanToInt(self, s: str) -> int:
        """Return integer represented by a string of Roman numerals, up to the M character."""
        roman: dict[str, int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i: int = 0
        sum: int = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                sum -= roman[s[i]]
            else:
                sum += roman[s[i]]
        sum += roman[s[len(s) - 1]]
        return sum
