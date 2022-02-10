
"""Looked at Solution"""

"""

Idea is that if you keep track of the sum in an array, 
if the sum at index i minus the sum at some later index j == k, then their elements 
make up a subarray whose sum is k. 

We keep track of these sums in a hashmap, and check to see if 
the sum(at current index) - k = a key (AKA sum at earlier index). 
If the sum is already in the hasmap, then we add 1 to it. 

Reason we add 1:
(Essentially saying that at some point an index's sum - k is equal to it, then there are 
two or more subarrays that start at different indexes, with the same sum whose elements
between it and the current index  would be equal to k.)

Finally,
If it is equal,then we know their elements are a subarray and 
add the amount stored in the map[sum - k] to the count.

"""
class Solution(object):
    def subarraySum(self, nums, k):
        map = {0:1}
        sum = 0 
        count = 0
        for i in nums:
            sum += i
            if sum - k in map:
                count += map[sum - k]
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
        return count