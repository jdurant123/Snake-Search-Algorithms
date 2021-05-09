from queue import Queue

from graph import canvas

from search import tools


def cal(start, end, obstacles=[], show_details=False):
    if tools.cell_equal(start, end):
        return []

    if tools.is_adjacent(start, end):
        return [end]

    queue = Queue()
    queue.put(start)
    mark = {tools.cal_cell_id(start): None}

    while not queue.empty():
        cell = queue.get()

        adjs = tools.adj(cell, mark, obstacles)
        for adj in adjs:
            if tools.cal_cell_id(adj) in mark.keys():
                continue

            mark[tools.cal_cell_id(adj)] = cell
            queue.put(adj)

            if tools.cell_equal(adj, end):
                path = tools.cal_path(mark, tools.cal_cell_id(adj))
                return path[1:] + [end]

            if show_details:
                canvas.draw_cell(adj, canvas.COLOR.DARK_GREEN.value)
                canvas.update()

    return None
