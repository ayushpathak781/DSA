class Solution:
    # Ayushpathak781
    def kLengthApart(self, nums, k):
        prev = -k - 1  

        for i, val in enumerate(nums):
            if val == 1:
                if i - prev <= k:  
                    return False
                prev = i
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.kLengthApart([1,0,0,0,1,0,0,1], 2))  
    print(s.kLengthApart([1,0,0,1,0,1], 2))    