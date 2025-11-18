class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_index = {}   # char -> last index seen
        start = 0         # left bound of current window
        max_len = 0
    #ayushpathak781
        for i, ch in enumerate(s):
            if ch in last_index and last_index[ch] >= start:
                start = last_index[ch] + 1
            last_index[ch] = i
            curr_len = i - start + 1
            if curr_len > max_len:
                max_len = curr_len

        return max_len