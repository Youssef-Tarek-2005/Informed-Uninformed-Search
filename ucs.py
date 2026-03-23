import heapq

#Uniform Cost Search
def ucs(graph, start, goal):
    heap = [(0, start, [])]
    visited = {} 
    steps = []
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node == goal: return path + [node], steps
        if node not in visited or cost < visited[node]:
            visited[node] = cost
            steps.append({'current': node, 'explored': list(visited.keys()), 
                          'frontier': [item[1] for item in heap], 'cost': cost})
            for neighbor, weight in graph.get(node, {}).items():
                heapq.heappush(heap, (cost + weight, neighbor, path + [node]))
    return None, steps

