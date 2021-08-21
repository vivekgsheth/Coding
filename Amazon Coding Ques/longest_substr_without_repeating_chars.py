from collections import defaultdict

def def_val():
    return -1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxm = 0
        d = defaultdict(def_val)
        n = len(s)
        while r < n:
            index = d[s[r]]    
            if index != -1 and index+1 > l:
                l = index+1
            d[s[r]] = r
            maxm = max(maxm, r-l+1)
            r += 1
        return maxm       
