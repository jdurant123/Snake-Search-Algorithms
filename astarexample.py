from search.a_star import cal

from graph import canvas

if __name__ == "__main__":
    canvas.init("A*")
    canvas.draw_bg()
    canvas.draw_grid()

    start = (6, 5)
    end = (12, 10)
    obstacles = []
    for x in range(4, 10):
        obstacles.append((x, 3))
    for x in range(4, 20):
        obstacles.append((x, 12))
    for y in range(2, 14):
        obstacles.append((10, y))
    for y in range(2, 16):
        obstacles.append((17, y))

    canvas.draw_cell(start, canvas.COLOR.GREEN.value)
    canvas.draw_cell(end, canvas.COLOR.RED.value)
    canvas.draw_cells(obstacles, canvas.COLOR.WHITE.value)
    canvas.update()

    input("Press <Enter> to start!")

    path = cal(start, end, obstacles, show_details=True)
    canvas.draw_cell_line(path[:-1], canvas.COLOR.DARK_GRAY.value, canvas.COLOR.RED.value)
    canvas.update()

    input("Press <Enter> to close!")
