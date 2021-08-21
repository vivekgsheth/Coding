def calculateSpan(self,a,n):
   #Nearest Greater To Left
   s = []
   idx = []
   for i in range(0, n):
       while len(s) != 0 and s[-1][0] <= a[i]:
           s.pop(-1)
       if len(s) == 0:
           idx.append(-1)
       else:
           idx.append(s[-1][1])
       s.append((a[i], i))
   res = [i - idx[i] for i in range(0, n)]
   return res
