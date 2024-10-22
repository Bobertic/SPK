from tkinter import *
import random, tkinter
from PIL import Image, ImageDraw, ImageTk
 

root = Tk()
root.title('Drawing Project')

cof = 5
tk_images = []

c = Canvas(root, width=6200 / cof, height=3400 / cof, bg='#fed48c')
c.pack()


import numpy as np

def ellips_cord(top_left, bottom_right, x_min, x_max, y_min, y_max, t):
    # Находим центр эллипса
    h = (top_left[0] + bottom_right[0]) / 2
    k = (top_left[1] + bottom_right[1]) / 2

    # Находим полуоси эллипса
    a = abs(bottom_right[0] - top_left[0]) / 2
    b = abs(bottom_right[1] - top_left[1]) / 2

    def generate_ellipse_points(h, k, a, b, num_points=100):
        t = np.linspace(0, 2 * np.pi, num_points)
        x = h + a * np.cos(t)
        y = k + b * np.sin(t)
        return np.column_stack((x, y))

    # Сгенерировать точки эллипса
    points = generate_ellipse_points(h, k, a, b)

    # Фильтрация точек по высоте и координатам x, y
    filtered_points = []
    for i in range(len(points)):
        if x_min <= points[i][0] <= x_max and y_min <= points[i][1] <= y_max:
            filtered_points.append([points[i][0], points[i][1]])

    print(filtered_points)

    # Преобразовать точки в список со списками и разделить на cof
    result_list = [[float(x) / cof, float(y) / cof] for x, y in filtered_points]

    return result_list[::t]

value1 = [[
    [2612, 2202],  # top_left
    [10438, 7882],  # bottom_right
    3350,  # x_min
    5177,  # x_max
    2389,  # y_min
    3400,  # y_max
    1  # t
],
[
    [3199, 7499],
    [10031, 2183],
    3744,
    5337,
    2376,
    3400,
    -1
]]

value2 = [[
    [2845, 1453],  # top_left
    [6835, 5443],  # bottom_right
    5868,  # x_min
    6200,  # x_max
    1738,  # y_min
    1989,  # y_max
    1  # t
],
[
    [3969, 1585],
    [6456, 4072],
    5829,
    6200,
    1749,
    2100,
    -1
]]
value = [[[
    [2612, 2202],  # top_left
    [10438, 7882],  # bottom_right
    3350,  # x_min
    5177,  # x_max
    2389,  # y_min
    3400,  # y_max
    1  # t
],
[
    [3199, 7499],
    [10031, 2183],
    3744,
    5337,
    2376,
    3400,
    -1
]],
[[
    [2845, 1453],  # top_left
    [6835, 5443],  # bottom_right
    5868,  # x_min
    6200,  # x_max
    1738,  # y_min
    1989,  # y_max
    -1  # t
],
[
    [3969, 1585],
    [6456, 4072],
    5829,
    6200,
    1749,
    2100,
    1
]]]

points = [[
    [3418 / cof, 3400 / cof],
    [5187 / cof, 2388 / cof, 5305 / cof, 2377 / cof],
    [3718 / cof, 3400 / cof]
],
[
    [6200 / cof, 2080 / cof],
    [5824 / cof, 1750 / cof, 5862 / cof, 1740 / cof],
    [6200 / cof, 1990 / cof]
]]

lst = []
lst1 = []
lst2 = []
for i in range(len(value)):
    lst.append(points[i][0])
    lst.append(ellips_cord(value[i][0][0], value[i][0][1], value[i][0][2], value[i][0][3], value[i][0][4], value[i][0][5], value[i][0][6]))
    lst.append(points[i][1])
    lst.append(ellips_cord(value[i][1][0], value[i][1][1], value[i][1][2], value[i][1][3], value[i][1][4], value[i][1][5], value[i][1][6]))
    lst.append(points[i][2])

    c.create_polygon(lst)
    lst = []
# for i in value2:
#     if i[6] == 1:
#         # lst2.append([i[2] / cof, i[5] / cof])
#         lst2.append(ellips_cord(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
#         # lst2.append([i[3] / cof, i[4] / cof])
#     else:
#         # lst2.append([i[3] / cof, i[4] / cof]) 
#         lst2.append(ellips_cord(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
#         # lst2.append([i[2] / cof, i[5] / cof])
# c.create_polygon(lst2)
root.mainloop()