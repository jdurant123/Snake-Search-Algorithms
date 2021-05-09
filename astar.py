from graph import canvas
from search.queue import PriorityQueue

from search import tools


def cal(start, end, obstacles=[], show_details=False):
    if tools.cell_equal(start, end):
        return []

    if tools.is_adjacent(start, end):
        return [end]

    queue = PriorityQueue()
    start_node = Node(start, 0, Node.cal_h(start, end))
    queue.put(start_node, start_node.f)
    mark = {tools.cal_cell_id(start): None}

    while not queue.empty():
        node = queue.get()

        adjs = tools.adj(node.cell, mark, obstacles)
        for adj in adjs:
            if tools.cal_cell_id(adj) in mark.keys():
                continue

            mark[tools.cal_cell_id(adj)] = node.cell

            adj_node = Node(adj, node.g + 1, Node.cal_h(adj, end))
            queue.put(adj_node, adj_node.f)

            if tools.cell_equal(adj, end):
                path = tools.cal_path(mark, tools.cal_cell_id(adj))
                return path[1:] + [end]

            if show_details:
                canvas.draw_cell(adj, canvas.COLOR.DARK_GREEN.value)
                canvas.update()

    return None


class Node:
    def __init__(self, cell, g, h):
        self._cell = cell
        self._g = g 
        self._h = h 
        self._f = g + h

    @property
    def cell(self):
        return self._cell

    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    @staticmethod
    def cal_h(cell1, cell2):
        (x1, y1) = cell1
        (x2, y2) = cell2
        return abs(x1 - x2) + abs(y1 - y2)
