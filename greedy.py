import heapq

#Greedy Best-First Search
def greedy(graph, start, goal, heuristics):

    heap = [(heuristics.get(start, 0), start, [])]  
    visited = set()
    steps = []

    while heap:
        heap.sort()  
        h_val, node, path = heapq.heappop(heap)

       
        frontier_view = [f"{n}(h={h})" for h, n, _ in heap]

        if node not in visited:
            visited.add(node)

            steps.append({
                'current': node,
                'explored': sorted(list(visited)),
                'frontier': frontier_view,
                'h': h_val
            })

            if node == goal:
                return path + [node], steps

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(heap, (heuristics.get(neighbor, 0), neighbor, path + [node]))

    return None, steps
