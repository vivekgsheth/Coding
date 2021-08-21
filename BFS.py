# your code goes here
# your code goes here
from collections import defaultdict

class Graph:
	def __init__(self):
		self.g = defaultdict(list)
	
	def add(self,u,v):
		self.g[u].append(v)
		# print(self.g)
	
	def __repr__(self):
		return self.g
		
	def bfs(self,s):
		q = []
		v = [False] * (max(self.g) + 1)
		v[s] = True
		q.append(s)
		# print(q)
		
		while q:
			s = q.pop(0)
			print(s,end=" ")
			for e in self.g[s]:
				if not v[e]:
					q.append(e)
					v[e] = True
lot = [	[1,0,0],
		[1,0,0],
		[1,9,1]]
		
g = Graph()
r = len(lot)
c = len(lot[0])
for i in range(0,r):
	for j in range(0,c):
		if (lot[i][j] == 1):
			g.add(i,j)
			# print(i,j)
			
g.bfs(0)
					