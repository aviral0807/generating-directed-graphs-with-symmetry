import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def draw():
    adjacency_matrix = np.genfromtxt('output.txt', dtype=int)
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.DiGraph(directed=True)
    gr.add_edges_from(edges)
    options = {
	    'node_color': 'blue',
	    'node_size': 500,
	    'width': 1,
	    'arrowstyle': '-|>',
	    'arrowsize': 12,
	}
    nx.draw_networkx(gr, arrows=True, **options)

    plt.show()

if __name__ == '__main__':
    draw()