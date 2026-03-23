# Informed-Uninformed-Search
This project is a complete Graph Searching System with an interactive GUI and visualization, designed to demonstrate and compare different search algorithms used in Artificial Intelligence.  The application allows users to build custom graphs, select a search strategy, and visually observe how the algorithm explores nodes to reach a target.

# 🧠 Graph Search Visualizer (GUI-Based)

A complete **Graph Searching System with GUI and Visualization** that demonstrates how different AI search algorithms work on user-defined graphs.

This project allows users to construct graphs, choose search algorithms, and visualize the process of finding a path from a start node to a goal node.

---

## 🚀 Features

### 🔍 Search Algorithms

#### Uninformed Search
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Iterative Deepening Search (IDS)
- Uniform Cost Search (UCS)

#### Informed Search
- Greedy Best-First Search
- A* Search

---

### 🧩 Graph Input
- Add nodes and edges manually
- Assign weights to edges
- Input heuristic values (for informed search)

---

### 📊 Visualization
- Interactive graph display
- Highlight explored nodes
- Highlight final path from start to goal

---

### 📍 Output
- Displays the found path
- Shows total path cost
- Shows message if no path exists

---

## 🖥️ GUI Overview

The graphical interface allows users to:
- Select a search algorithm
- Enter nodes and edges
- Define weights and heuristics
- Choose start and goal nodes
- Run and visualize the search

---

## ⚙️ How It Works

1. The user inputs the graph (nodes, edges, weights).
2. Selects a search algorithm.
3. If using informed search, heuristic values are provided.
4. The system runs the algorithm and:
   - Finds the path (if it exists)
   - Calculates total cost
   - Displays a visual representation of the search process

---

## 🛠️ Technologies Used

- **Python**
- **Tkinter / PyQt** (for GUI)
- **NetworkX** (graph handling)
- **Matplotlib** (visualization)

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/graph-search-visualizer.git
