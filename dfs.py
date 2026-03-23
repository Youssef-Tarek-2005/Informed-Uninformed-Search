from collections import deque

#Depth-First Search
def dfs(graph, start, goal=None):
    if not goal:
        
        visited = set()
        stack = [start]
        order = []
        steps = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                steps.append({'current': node, 'explored': list(visited), 'frontier': list(stack)})
                for neighbor in reversed(graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order, steps
    
   
    visited = set()
    stack = [start]
    parent = {start: None}
    steps = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            steps.append({'current': node, 'explored': list(visited), 'frontier': list(stack)})
            
            if node == goal:
                
                path = []
                current = goal
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path, steps
            
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    parent[neighbor] = node
                    stack.append(neighbor)
    
    return None, steps

