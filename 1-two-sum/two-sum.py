class Solution:
    def twoSum(self, nums, target):
        #ayushpathak781
        seen = {} 
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        raise ValueError("No two sum solution")