# Create a graph 
graph = {}
costs = {}
parents = {}
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_code_node = None

    global processed

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_code_node = node

    return lowest_code_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

# Printing the path
path = ["F"]
node = "F"
while node is not None:
    new_node = parents[node]
    path.append(new_node)
    
    node = new_node