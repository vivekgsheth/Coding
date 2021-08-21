class Solution:
    def nsl(self, arr, n):
        s = []
        idx = []
        pseudo_idx = -1
        for i in range(0, n):
            while len(s) != 0 and s[-1][0] >= arr[i]:
                s.pop(-1)
            if len(s) == 0:
                idx.append(pseudo_idx)
            else:
                idx.append(s[-1][1])
            s.append((arr[i], i))
        return idx
        
    def nsr(self, arr, n):
        s = []
        idx = []
        pseudo_idx = n
        for i in range(n-1, -1, -1):
            while len(s) != 0 and s[-1][0] >= arr[i]:
                s.pop(-1)
            if len(s) == 0:
                idx.append(pseudo_idx)
            else:
                idx.append(s[-1][1])
            s.append((arr[i], i))
        idx.reverse()
        return idx
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        nsl_idx = self.nsl(heights, len(heights))
        nsr_idx = self.nsr(heights, len(heights))
        n = len(heights)
        width = [nsr_idx[i]-nsl_idx[i]-1 for i in range(0, n)]
        area = [width[i]*heights[i] for i in range(0, n)]
        return max(area)
