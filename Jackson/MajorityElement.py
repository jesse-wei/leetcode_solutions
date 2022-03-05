class Solution(object):
    def majorityElement(self, nums):
        map ={}
        sol = 0
        compare = 0
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1
        for i in map:
            if map[i] > compare:
                sol = i
                compare = map[i]
                
        return sol
            
            
            
            