class Solution:
    def twoSum(self, nums, target):
        seen = {} #ayushpathak781
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        raise ValueError("No two sum solution")