# Graph Search Visualizer 🖥️🔍

This project is a complete Graph Searching System with a graphical user interface and visualization. It demonstrates the behavior of different search algorithms used in Artificial Intelligence by allowing users to construct graphs, execute search strategies, and observe the results visually.

---

## Features ✨

### Supported Algorithms 🧠

#### Uninformed Search 🚦
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Iterative Deepening Search (IDS)
- Uniform Cost Search (UCS)

#### Informed Search 🏁
- Greedy Best-First Search
- A* Search

---

## Graph Input 📊

Users can define a custom graph by entering:  
- Graph structure (adjacency list format)  
- Node costs (weights)  
- Heuristic values (for informed search)

---

## GUI Functionality 🖱️

- Select search algorithm  
- Input graph structure, node costs, and heuristics  
- Enter start and goal nodes  
- Execute the algorithm  
- Step-by-step table showing:
  - Current node 🟢  
  - Explored nodes 🔶  
  - Frontier ⏳  
  - Cost and heuristic values 📈  

---

## Output 📌

- Displays the final path if found ✅  
- Shows total path cost with detailed breakdown 💰  
- Message if no path exists ❌  
- Graph visualization with highlighted nodes and path 🎨  

---

## Visualization 🌐

- Default nodes: light blue  
- Explored nodes: orange  
- Final path: green  
- Goal node: red  

Uses **NetworkX** and **Matplotlib** for dynamic graph rendering.

---

## Technologies Used 🛠️

- Python 🐍  
- Tkinter (GUI) 🖥️  
- NetworkX 📈  
- Matplotlib 🎨  

---

## How to Run ▶️

1. Clone the repository:
git clone https://github.com/your-username/Graph-Search-Visualizer.git
z
2. Navigate to the project directory:
cd "Graph Search Visualizer"

3. Install required libraries:
pip install networkx matplotlib

4. Run the GUI application:
python app.py


## Project Structure 📂
Graph Search Visualizer/
├── app.py            # Main GUI application
├── bfs.py            # Breadth-First Search implementation
├── dfs.py            # Depth-First Search implementation
├── ids.py            # Iterative Deepening Search implementation
├── ucs.py            # Uniform Cost Search implementation
├── greedy.py         # Greedy Best-First Search implementation
├── astar.py          # A* Search implementation

## Purpose 🎯

This project is designed for educational purposes to help understand and compare different graph search algorithms, including both uninformed and informed approaches, with a visual and interactive approach.

Future Improvements 🔧
Step-by-step animation controls
Save and load graph configurations
Performance comparison between algorithms
Support for directed graphs


## Author 👤

Youssef Tarek Mohamed

## License 📄

This project is intended for educational purposes.

