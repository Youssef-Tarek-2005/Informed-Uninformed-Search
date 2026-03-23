#Iterative Deepening Search
def ids(graph, start, goal):
    steps = []
    def dls(node, depth, path, visited):
        visited.add(node)
        steps.append({'current': node, 'explored': list(visited), 'frontier': [f"Depth:{depth}"]})
        if node == goal: return path + [node]
        if depth <= 0: return None
        for neighbor in graph.get(node, []):
            if neighbor not in path: 
                result = dls(neighbor, depth-1, path + [node], visited)
                if result: return result
        return None

    depth = 0
    while depth < 100: 
        visited = set()
        result = dls(start, depth, [], visited)
        if result: return result, steps
        depth += 1
    return None, steps
