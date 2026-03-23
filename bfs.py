from collections import deque
#Breadth-First Search
def bfs(graph, start, goal=None):
    if not goal:
       
        visited = set()
        queue = deque([start])
        order = []
        steps = []
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                steps.append({'current': node, 'explored': list(visited), 'frontier': list(queue)})
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return order, steps
    

    visited = set()
    queue = deque([start])
    parent = {start: None}
    steps = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            steps.append({'current': node, 'explored': list(visited), 'frontier': list(queue)})
            
            if node == goal:
               
                path = []
                current = goal
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path, steps
            
            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    parent[neighbor] = node
                    queue.append(neighbor)
    
    return None, steps
