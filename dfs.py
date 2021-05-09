from queue import LifoQueue

from graph import canvas

from search import tools


def cal(start, end, obstacles=[], show_details=False):
    if tools.cell_equal(start, end):
        return []

    if tools.is_adjacent(start, end):
        return [end]

    queue = LifoQueue()
    mark = {}

    queue.put(Node(start))

    while not queue.empty():
        node = queue.get()
        cell = node.cell
        parent = node.parent

        if tools.cal_cell_id(cell) in mark.keys():
          
            continue

        mark[tools.cal_cell_id(cell)] = parent

        if show_details:
            canvas.draw_cell(cell, canvas.COLOR.DARK_GREEN.value)
            canvas.update()

        if tools.cell_equal(cell, end):
            path = tools.cal_path(mark, tools.cal_cell_id(end))
            return path[1:] + [end]

        adjs = tools.adj(cell, mark, obstacles)
        for adj in adjs:
            queue.put(Node(adj, cell))

    return None


class Node:
    def __init__(self, cell, parent=None):
        self._cell = cell
        self._parent = parent

    @property
    def cell(self):
        return self._cell

    @property
    def parent(self):
        return self._parent
