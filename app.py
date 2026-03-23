import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from bfs import bfs
from dfs import dfs
from ids import ids
from ucs import ucs
from greedy import greedy
from astar import astar


BG, PANEL, TEXT, ACCENT = "#0f0f1a", "#1a1a2e", "#e0e0ff", "#4488ff"
GREEN, RED, ORANGE, MUTED = "#00ff88", "#ff4466", "#ffaa00", "#7788aa"

class GraphSearchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Searching Algorithms")
        self.geometry("850x600")
        self.configure(bg=BG)
        self.algorithm = tk.StringVar(value="BFS")
        self._build_scrollable_ui()
        self._load_defaults()

    def _build_scrollable_ui(self):
        container = tk.Frame(self, bg=BG)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=BG, highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        v_scroll = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        v_scroll.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=v_scroll.set)

        scroll_frame = tk.Frame(canvas, bg=BG)
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

        self._build_ui(scroll_frame)

    def _build_ui(self, parent):
        tk.Label(parent, text="Searching Algorithms", bg=BG, fg=ACCENT, font=("Arial", 22, "bold")).pack(pady=10)
        main_container = tk.Frame(parent, bg=BG)
        main_container.pack(fill="both", expand=True, padx=20)

      
        left_panel = tk.Frame(main_container, bg=BG, width=380)
        left_panel.pack(side="left", fill="y", padx=10)

        algo_box = tk.LabelFrame(left_panel, text="1. Algorithm", bg=BG, fg=TEXT, padx=5, pady=5)
        algo_box.pack(fill="x", pady=5)
        for i, name in enumerate(["BFS", "DFS", "IDS", "UCS", "Greedy", "A*"]):
            tk.Radiobutton(algo_box, text=name, variable=self.algorithm, value=name, bg=BG, fg=TEXT, selectcolor=PANEL).grid(row=i//3, column=i%3, sticky="w", padx=10)

        tk.Label(left_panel, text="2. Graph (Node:Neigh1,Neigh2)", bg=BG, fg=ACCENT).pack(anchor="w")
        self.txt_graph = tk.Text(left_panel, height=8, bg=PANEL, fg=TEXT, font=("Consolas", 10))
        self.txt_graph.pack(fill="x", pady=5)

        tk.Label(left_panel, text="3. Weights/Real Cost (Node:Val)", bg=BG, fg=ACCENT).pack(anchor="w")
        self.txt_data = tk.Text(left_panel, height=5, bg=PANEL, fg=TEXT, font=("Consolas", 10))
        self.txt_data.pack(fill="x", pady=5)


        tk.Label(left_panel, text="4. Heuristics Cost (Node:H)", bg=BG, fg=ACCENT).pack(anchor="w")
        self.txt_heuristic = tk.Text(left_panel, height=5, bg=PANEL, fg=TEXT, font=("Consolas", 10))
        self.txt_heuristic.pack(fill="x", pady=5)

        sg_frame = tk.Frame(left_panel, bg=BG)
        sg_frame.pack(fill="x", pady=5)
        self.ent_start = self._create_input(sg_frame, "Start:", 0)
        self.ent_goal = self._create_input(sg_frame, "Goal:", 1)

        tk.Button(left_panel, text="CALCULATE PATH", command=self._run, bg=GREEN, fg=BG, font=("Arial", 11, "bold")).pack(fill="x", pady=10)
        
        self.table = ttk.Treeview(left_panel, columns=("step", "current", "explored", "frontier", "extra"), show="headings", height=8)
        self.table.heading("step", text="Step"); self.table.heading("current", text="Current")
        self.table.heading("explored", text="Explored"); self.table.heading("frontier", text="Frontier")
        self.table.heading("extra", text="Algorithm Info")
        self.table.column("step", width=60); self.table.column("current", width=80)
        self.table.column("explored", width=150); self.table.column("frontier", width=150)
        self.table.column("extra", width=120)
        self.table.pack(fill="both", expand=True)

        
        right_panel = tk.Frame(main_container, bg=PANEL)
        right_panel.pack(side="right", fill="both", expand=True)
        self.fig_container = tk.Frame(right_panel, bg=PANEL)
        self.fig_container.pack(fill="both", expand=True)
        
        
        self.lbl_path = tk.Label(right_panel, text="Path: --", bg=PANEL, fg=TEXT, font=("Courier", 12))
        self.lbl_path.pack()
        self.lbl_cost = tk.Label(right_panel, text="TOTAL COST: 0", bg=PANEL, fg=GREEN, font=("Courier", 16, "bold"), pady=10)
        self.lbl_cost.pack()

    def _create_input(self, parent, label, col):
        f = tk.Frame(parent, bg=BG)
        f.grid(row=0, column=col, padx=10)
        tk.Label(f, text=label, bg=BG, fg=TEXT).pack()
        e = tk.Entry(f, width=10, bg=PANEL, fg=TEXT, justify="center")
        e.pack(); return e

    def _load_defaults(self):
        self.txt_graph.insert("1.0", "A:B,C,D\nB:E,F\nC:G,H\nD:I,J\nE:K\nF:L\nI:M\nG:\nH:\nJ:\nK:\nL:\nM:")
        self.txt_data.insert("1.0", "A:10,B:5,C:7,D:3,E:2,F:3,G:2,H:1,I:5,J:2,K:1,L:3,M:0")
        self.txt_heuristic.insert("1.0", "A:10,B:8,C:6,D:7,E:5,F:4,G:3,H:2,I:4,J:2,K:1,L:1,M:0")
        self.ent_start.insert(0, "A"); self.ent_goal.insert(0, "M")

    def _run(self):
        self.table.delete(*self.table.get_children())
        graph = {}
        for line in self.txt_graph.get("1.0", "end").split("\n"):
            if ":" in line:
                n, neighs = line.split(":")
                graph[n.strip().upper()] = [x.strip().upper() for x in neighs.split(",") if x.strip()]
        
        data = {}
        for p in self.txt_data.get("1.0", "end").replace("\n", ",").split(","):
            if ":" in p:
                k, v = p.split(":")
                data[k.strip().upper()] = float(v.strip())

        heuristic = {}
        for p in self.txt_heuristic.get("1.0", "end").replace("\n", ",").split(","):
            if ":" in p:
                k, v = p.split(":")
                heuristic[k.strip().upper()] = float(v.strip())

        weighted_g = {n: {nb: data.get(nb, 1) for nb in neighs} for n, neighs in graph.items()}
        s, g = self.ent_start.get().strip().upper(), self.ent_goal.get().strip().upper()
        algo = self.algorithm.get()

        try:
            res_path, steps = None, []
            if algo == "BFS": 
                res_path, steps = bfs(graph, s, g)
            elif algo == "DFS": 
                res_path, steps = dfs(graph, s, g)
            elif algo == "IDS": 
                res_path, steps = ids(graph, s, g)
            elif algo == "UCS": 
                res_path, steps = ucs(weighted_g, s, g)
            elif algo == "Greedy": 
                res_path, steps = greedy(graph, s, g, data)
            elif algo == "A*": 
                res_path, steps = astar(graph, s, g, data, data)

            for item in self.table.get_children():
                self.table.delete(item)
            
            for i, st in enumerate(steps):
                current = st['current']
                explored = ', '.join(st.get('explored', []))
                frontier = ', '.join(st.get('frontier', []))
                
                extra_info = []
                if 'cost' in st:
                    extra_info.append(f"Cost:{st['cost']:.1f}")
                if 'h' in st:
                    extra_info.append(f"H:{st['h']:.1f}")
                if 'g' in st:
                    extra_info.append(f"G:{st['g']:.1f}")
                
                extra_str = ' | '.join(extra_info) if extra_info else '-'
                
                self.table.insert("", "end", values=(f"Step {i+1}", current, explored, frontier, extra_str))

            if res_path:
                total_cost = 0
                cost_breakdown = []
                for i in range(len(res_path)-1):
                    current_node = res_path[i]
                    next_node = res_path[i+1]
                    edge_cost = data.get(next_node, 1)
                    total_cost += edge_cost
                    cost_breakdown.append(f"{current_node}->{next_node}={edge_cost}")
                
                path_with_costs = " -> ".join([f"{node}({data.get(node,0)})" for node in res_path])
                self.lbl_path.config(text=f"PATH: {path_with_costs}")
                self.lbl_cost.config(text=f"TOTAL COST: {total_cost} | {' + '.join(cost_breakdown)}")
                self._draw_graph(graph, res_path, [st['current'] for st in steps])
            else:
                self.lbl_path.config(text="No path found."); self.lbl_cost.config(text="TOTAL COST: N/A")
        except Exception as e: messagebox.showerror("Error", str(e))

    def _draw_graph(self, graph, path, expanded):
        for w in self.fig_container.winfo_children(): w.destroy()
        
        G = nx.Graph()
        for n, neigh in graph.items():
            if isinstance(neigh, dict):
                for nb in neigh:
                    G.add_edge(n, nb)
            else:
                for nb in neigh:
                    G.add_edge(n, nb)

        pos = nx.spring_layout(G, seed=42)
        
        fig = Figure(figsize=(6, 4), facecolor=PANEL)
        ax = fig.add_subplot(111)
        ax.set_facecolor(PANEL)
        
        goal = self.ent_goal.get().strip().upper()
        
        nx.draw(G, pos, ax=ax, with_labels=True, node_color="lightblue", 
                font_color="black", node_size=800, font_size=12, font_weight='bold')
        
        if expanded:
            nx.draw_networkx_nodes(G, pos, nodelist=expanded, node_color="orange", ax=ax, node_size=1000)
        
        if path:
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="green", ax=ax, node_size=1200)
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="green", 
                                 width=4, ax=ax, alpha=0.8)
            
            if goal and goal in path:
                nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color="red", 
                                      ax=ax, node_size=1300, edgecolors="red", linewidths=4)
        
        ax.set_axis_off()
        
        canvas = FigureCanvasTkAgg(fig, master=self.fig_container)
        canvas.draw(); canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    app = GraphSearchApp()
    app.mainloop()