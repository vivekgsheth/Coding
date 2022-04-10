from collections import defaultdict
import queue

t = int(input())
while t:
    graph = defaultdict(list)
    t-=1
    n = int(input())
    for u in range(0,n):
        ip = list(map(int ,input().split()))
        for v in range(0,len(ip)):
            if ip[v] != 0:
                graph[u].append((v,ip[v]))
    print(graph)
    q = queue.PriorityQueue()
    q.put((0,0))
    max_val = 99999
    dist = [max_val] * n
    dist[0] = 0

    while not q.empty():
        curr = q.get()
        print(curr)
        curr_node  = curr[1]
        curr_dist = curr[0]
        for child in graph[curr_node]:
            print(child)
            child_node = child[0]
            edge_dist = child[1]
            if curr_dist+edge_dist < dist[child_node]:
                dist[child_node] = curr_dist+edge_dist
                q.put((dist[child_node],child_node))
    print(dist)