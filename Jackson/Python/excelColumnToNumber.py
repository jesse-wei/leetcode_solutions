"""
Rrlationship between Column and Numbers are:

26^(length of string - 1) * (difference between A and Number + 1)

AB

26^1 * 1   +  2

28

"""
class Solution(object):
    def titleToNumber(self, columnTitle):
        x = ord('A')
        sol = 0
        l = len(columnTitle) - 1
        for i in range(len(columnTitle)):
            m = (ord(columnTitle[i]) - ord('A')) + 1
            if l >= 1:
                sol += (26**l) * m
                print(sol)
            else:
                sol += m
            l -= 1
        return sol