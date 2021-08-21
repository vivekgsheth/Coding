class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        mxL = [-1] * n
        mxR = [-1] * n
        water = [-1] * n
        mxL[0] = height[0]
        mxR[n-1] = height[-1]
        
        for i in range(1, n):
            mxL[i] = max(mxL[i-1], height[i])
            
        for i in range(n-2, -1, -1):
            mxR[i] = max(mxR[i+1], height[i])
        
        print("mxL", mxL)
        print("mxR", mxR)
        for i in range(0, n):
            water[i] = min(mxL[i], mxR[i]) - height[i]
        
        return sum(water)
            
