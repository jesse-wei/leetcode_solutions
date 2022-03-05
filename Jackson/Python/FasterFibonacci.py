"""Storing values so work is not Repeated."""
class Solution(object):
    def fib(self, n):
        map = {}
        return self.recurse(n, map)
    def recurse(self, n, map):
        if n in map:
            return map[n]
        if n <= 1:
            return n
        else:
            map[n] = self.recurse(n - 1, map) + self.recurse(n - 2, map)
            return map[n]
        
        
    