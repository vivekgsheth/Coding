
class Solution:
    def nextLargerElement(self,arr,n) -> list:
        s = []
        ans = []
        
        for i in range(n-1,-1,-1):
            while len(s) != 0 and s[-1] <= arr[i]:
                s.pop(-1)
            if len(s) == 0:
                ans.append(-1)
            else:
                ans.append(s[-1])
            s.append(arr[i])
        ans.reverse()
        # print(ans)
        return ans     
