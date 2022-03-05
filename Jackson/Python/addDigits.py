class Solution(object):
    def addDigits(self, num):
        """Recursively adds digits of a number until the result only has 1 digit"""
        s = str(num)
        sol = 0
        for i in s:
            sol += int(i)
        if abs(sol) < 10:
            return sol
        else:
            return self.addDigits(sol)
            