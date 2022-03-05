"""Looked at all the Hints"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        map = {}
        map2 = {}
        counter = 0
        
        """EDGE CASES"""
        if len(s1) > len(s2):
            return False
        if len(s1) == 1:
            if s1[0] in s2:
                return True
            else:
                return False
        """ALGO: Sliding Window"""
        """Creates a frequency Hash for the s1 String"""
        for j in s1:
            if j not in map2:
                map2[j] = 1
            else:
                map2[j] += 1
            
        
        """Create a frequency hash for s2."""
        for i in s2:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
            """When the index(counter) is greater than or equal to the length of the string,
            go to the frequency key at that index and either remove it or decrease it by 1"""
            if counter >= len(s1):
                if map[s2[counter - len(s1)]] == 1:
                    del map[s2[counter - len(s1)]]
                else:
                    map[s2[counter - len(s1)]] -=1
            """If the maps are ever equal, it means a permutation exists."""
            if map == map2:
                return True
            counter += 1
        return False


""""Example:

"ab", "asfbacd"

map2 = {a:1, b:2}

iteration start:

(a)

map = {a:1}

counter = 1

(s)

map = {a:1, s:1}

counter = 2

(f)

map = {a:1, s:1, f:1}

counter >= len(string)
    decrease char at counter - len(string)

map = {s:1, f:1}

counter = 3

(b)

map = {s:1, f:1, b:1}

counter >= len(string)
    decrease char at counter - len(string)

map = {f:1, b:1}

counter = 4

(a)

map = {f:1, b:1, a:1}

counter >= len(string)
    decrease char at counter - len(string)

map = {b:1, a:1}

map == map2
    return True
"""



        
        