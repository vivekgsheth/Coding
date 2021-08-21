def knapSack(self,W, wt, val, n):
  
   # code here
   rows, cols = (n+1, W+1)
   t = [[-1 for i in range(cols)] for j in range(rows)]
   # print(t)
   for i in range(0,rows):
       for j in range(0,cols):
           if i==0  or j==0:
               t[i][j] = 0
               
   # print(t)
   # print(t[1][0]) 
   
   for i in range(1,rows):
       for j in range(1,cols):
           
           if wt[i-1] <= j:
               t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
           else:
               t[i][j] = t[i-1][j]
               
   return t[n][W]
