class Solution(object):
    def twoSum(self, nums, target):
        sums = {}
        for i in range(len(nums)):
            thing = target - nums[i]
            if thing in sums:  
                return [sums[thing], i]
            else:
                sums[nums[i]] = i