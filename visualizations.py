import numpy as np
import math
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

united_states_map = mpimg.imread("united_states_map.png")


def show_cities(path, w=12, h=8):
    """Plot a TSP path overlaid on a map of the US States & their capitals."""
    if isinstance(path, dict):      path = list(path.values())
    if isinstance(path[0][0], str): path = [item[1] for item in path]
    plt.imshow(united_states_map)
    for x0, y0 in path:
        plt.plot(x0, y0, 'y*', markersize=15)  # y* = yellow star for starting point
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])
    plt.show()


def show_path(path, starting_city=None, w=12, h=8):
    """Plot a TSP path overlaid on a map of the US States & their capitals."""
    if isinstance(path, dict):      path = list(path.values())
    if isinstance(path[0][0], str): path = [item[1] for item in path]

    starting_city = starting_city or path[0]
    x, y = list(zip(*path))
    # _, (x0, y0) = starting_city
    (x0, y0) = starting_city
    plt.imshow(united_states_map)
    # plt.plot(x0, y0, 'y*', markersize=15)  # y* = yellow star for starting point
    plt.plot(x + x[:1], y + y[:1])  # include the starting point at the end of path
    plt.axis("off")
    fig = plt.gcf()
    fig.set_size_inches([w, h])


def polyfit_plot(x, y, deg, **kwargs):
    coefficients = np.polyfit(x, y, deg, **kwargs)
    poly = np.poly1d(coefficients)
    new_x = np.linspace(x[0], x[-1])
    new_y = poly(new_x)
    plt.plot(x, y, "o", new_x, new_y)
    plt.xlim([x[0] - 1, x[-1] + 1])

    terms = []
    for p, c in enumerate(reversed(coefficients)):
        term = str(round(c, 1))
        if p == 1:
            term += 'x'
        if p >= 2:
            term += 'x^' + str(p)
        terms.append(term)
    plt.title(" + ".join(reversed(terms)))


def distance(xy1, xy2) -> float:
    if isinstance(xy1[0], str):
        xy1 = xy1[1]
        xy2 = xy2[1]  # if xy1 == ("Name", (x,y))
    return math.sqrt((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2)


def path_distance(path) -> int:
    if isinstance(path, dict):
        path = list(path.values())  # if path == {"Name": (x,y)}
    if isinstance(path[0][0], str):
        path = [item[1] for item in path]  # if path == ("Name", (x,y))
    return int(sum(
        [distance(path[i], path[i + 1]) for i in range(len(path) - 1)]
        + [distance(path[-1], path[0])]  # include cost of return journey
    ))

# cities = { "Oklahoma City": (392.8, 356.4), "Montgomery": (559.6, 404.8), "Saint Paul": (451.6, 186.0), "Trenton": (698.8, 239.6), "Salt Lake City": (204.0, 243.2), "Columbus": (590.8, 263.2), "Austin": (389.2, 448.4), "Phoenix": (179.6, 371.2), "Hartford": (719.6, 205.2), "Baton Rouge": (489.6, 442.0), "Salem": (80.0, 139.2), "Little Rock": (469.2, 367.2), "Richmond": (673.2, 293.6), "Jackson": (501.6, 409.6), "Des Moines": (447.6, 246.0), "Lansing": (563.6, 216.4), "Denver": (293.6, 274.0), "Boise": (159.6, 182.8), "Raleigh": (662.0, 328.8), "Atlanta": (585.6, 376.8), "Madison": (500.8, 217.6), "Indianapolis": (548.0, 272.8), "Nashville": (546.4, 336.8), "Columbia": (632.4, 364.8), "Providence": (735.2, 201.2), "Boston": (738.4, 190.8), "Tallahassee": (594.8, 434.8), "Sacramento": (68.4, 254.0), "Albany": (702.0, 193.6), "Harrisburg": (670.8, 244.0) }
# cities = list(sorted(cities.items()))
# print(len(cities))
# #show_cities(cities)
#
# print(path_distance(cities))
