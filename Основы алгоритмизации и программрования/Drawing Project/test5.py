from tkinter import *
import random, tkinter
from PIL import Image, ImageDraw, ImageTk
from math import sin, cos, pi

root = Tk()
root.title('Drawing Project')

cof = 5
tk_images = []

c = Canvas(root, width=6200 / cof, height=3400 / cof, bg='#fed48c')
c.pack()

def ellips(top_left, bottom_right, amount, x_minmax, y_minmax, t):
    if abs(top_left[0] + bottom_right[0]) > abs(top_left[1] - bottom_right[1]):
        major_axis = abs(top_left[0] + bottom_right[0]) / 2
        minor_axis = abs(top_left[1] + bottom_right[1]) / 2
    else:
        minor_axis = abs(top_left[0] + bottom_right[0]) / 2
        major_axis = abs(top_left[1] + bottom_right[1]) / 2

    print(major_axis, minor_axis)
    center = [abs(top_left[0] - bottom_right[0]), abs(top_left[1] - bottom_right[1])]

    lst_def = []

    for i in range(amount):
        x_lst = major_axis * cos(i * 2 * pi / amount) + center[0]
        y_lst = minor_axis * sin(i * 2 * pi / amount) + center[1]
        print(x_minmax, x_lst, y_minmax, y_lst)
        if x_minmax[0] < x_lst < x_minmax[1] and y_minmax[0] < y_lst < y_minmax[1]:
            lst_def.append([x_lst / cof, y_lst / cof])

    return lst_def[::t]


values_1 = [[
    [2296, 2272],
    [9984, 9960],
    400,
    1
]]
points_1 = [[
    [3419, 3400],
    [5212, 2385]
]]

lst_1 = []

for i in range(len(values_1)):
    lst_1.append([points_1[i][0][0] / cof, points_1[i][0][1] / cof])
    lst_1.append(ellips(values_1[i][0], values_1[i][1], values_1[i][2], [points_1[i][0][0], points_1[i][1][0]], [points_1[i][1][1], points_1[i][0][1]], values_1[i][3]))
    lst_1.append([points_1[i][1][0] / cof, points_1[i][1][1] / cof])


c.create_polygon(lst_1)



root.mainloop()