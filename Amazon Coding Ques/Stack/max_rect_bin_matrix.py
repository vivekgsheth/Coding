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
    
    def mah(self, arr, m):
        nsl_idx = self.nsl(arr, m)
        nsr_idx = self.nsr(arr, m)
        print("nsl", nsl_idx)
        print("nsr", nsr_idx)
        width = [nsr_idx[i]-nsl_idx[i]-1 for i in range(0, m)]
        area = [width[i]*arr[i] for i in range(0, m)]
        return max(area)
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        v = []
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        for i in range(0, n):
            matrix[i] = list(map(int, matrix[i]))    
        # print(matrix)
        # print(n, m)
        for j in range(0 ,m):
            v.append(matrix[0][j])
        print("v", v)
        maxm = self.mah(v, m)
        print("mah[0]", maxm)
        for i in range(1, n):
            for j in range(0, m):
                if matrix[i][j] == 0:
                    v[j] = 0
                else:
                    v[j] += matrix[i][j]
            print("v", i , v)
            maxm = max(maxm, self.mah(v, m))
            print("maxm", maxm)
        return maxm
