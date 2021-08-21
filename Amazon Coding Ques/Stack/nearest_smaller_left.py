def immediateSmaller(self,arr,n):
	# code here
	ans = []
	s = []
	for i in range(0, n):
	    while len(s) != 0 and s[-1] >= arr[i]:
	        s.pop(-1)
        if len(s) == 0:
            ans.append(-1)
       else:
           ans.append(s[-1])
       s.append(arr[i])
   return ans

