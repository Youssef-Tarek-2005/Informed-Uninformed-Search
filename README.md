Graph Search Visualizer (GUI-Based)

This project is a complete Graph Searching System with a graphical user interface and visualization. It demonstrates the behavior of different search algorithms used in Artificial Intelligence by allowing users to construct graphs, execute search strategies, and observe the results visually.

Features
Supported Algorithms
Uninformed Search
Breadth-First Search (BFS)
Depth-First Search (DFS)
Iterative Deepening Search (IDS)
Uniform Cost Search (UCS)
Informed Search
Greedy Best-First Search
A* Search
Graph Input

Users can define a custom graph using the following inputs:

Graph Structure (Adjacency List)

Each line represents a node and its neighbors:
A:B,C,D
B:E,F
C:G,H

Node Costs (Weights)

Used for cost-based algorithms:
A:10,B:5,C:7,D:3

Heuristic Values

Used for informed search algorithms:
A:10,B:8,C:6,D:7

GUI Functionality
Selection of search algorithm
Input fields for graph structure, node costs, and heuristics
Entry of start and goal nodes
Execution button to run the selected algorithm
Step-by-step execution table displaying:
Current node
Explored nodes
Frontier
Additional algorithm-specific data (cost, heuristic, etc.)
Output
Displays the final path if found
Shows total path cost with detailed breakdown
Displays a message if no path exists
Visualizes the graph with:
Explored nodes highlighted
Final path clearly marked
Goal node emphasized
Visualization

The system uses NetworkX and Matplotlib to render the graph dynamically:

Default nodes are displayed in light blue
Explored nodes are highlighted in orange
Final path is highlighted in green
Goal node is highlighted in red
Technologies Used
Python
Tkinter (GUI)
NetworkX (Graph representation)
Matplotlib (Graph visualization)
How to Run
Clone the repository:
git clone https://github.com/your-username/graph-search-visualizer.git
Navigate to the project directory:
cd graph-search-visualizer
Install required libraries:
pip install networkx matplotlib
Run the application:
python main.py
Project Structure

main.py
bfs.py
dfs.py
ids.py
ucs.py
greedy.py
astar.py

Purpose

This project is intended for educational use to help understand and compare different graph search algorithms, including both uninformed and informed approaches. It provides a visual and interactive way to study how these algorithms explore graphs and determine optimal paths.

Future Improvements
Step-by-step animation controls
Save and load graph configurations
Performance comparison between algorithms
Support for directed graphs
Author

Your Name

License

This project is intended for educational purposes.
