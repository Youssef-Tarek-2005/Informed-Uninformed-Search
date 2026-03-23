import heapq

#A* Search
def astar(graph, start, goal, heuristics, weights):
    
    heap = [(heuristics.get(start, 0), 0, start, [])] 
    visited = {}
    steps = []

    while heap:
        heap.sort()  
        f, g, node, path = heapq.heappop(heap)

        
        frontier_view = [f"{n}(f={f_val},g={g_val},h={heuristics.get(n,0)})" 
                         for f_val, g_val, n, _ in heap]

        if node not in visited or g < visited[node]:
            visited[node] = g

            steps.append({
                'current': node,
                'explored': sorted(list(visited.keys())),
                'frontier': frontier_view,
                'g': g,
                'h': heuristics.get(node, 0),
                'f': f
            })

            if node == goal:
                return path + [node], steps

            for neighbor in graph.get(node, []):
                new_g = g + weights.get(neighbor, 1)
                new_h = heuristics.get(neighbor, 0)
                new_f = new_g + new_h

                heapq.heappush(heap, (new_f, new_g, neighbor, path + [node]))

    return None, steps