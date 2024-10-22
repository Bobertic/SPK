from tkinter import *
import random, tkinter
from PIL import Image, ImageDraw, ImageTk
 

root = Tk()
root.title('Drawing Project')

cof = 5
tk_images = []

c = Canvas(root, width=6200 / cof, height=3400 / cof, bg='#fed48c')
c.pack()

number = int(2000 / cof)
for i in range(number):
    color = "#{:02x}{:02x}{:02x}".format(255, int(159 + 73 / number * i), int(98 + 97 / number * i))
    c.create_line(0, i, 6200 / cof, i, fill=color)


def triangle_1(x, y, color):
    c.create_polygon((x - 236) / cof, (y + 769) / cof,
                     x / cof, y / cof,
                     (x + 179) / cof, (y + 769) / cof,
                     fill = color)

def triangle_2(x, y, color):
    c.create_polygon((x - 254) / cof, (y + 641) / cof,
                     x / cof, y / cof,
                     (x + 213) / cof, (y + 641) / cof,
                     fill = color)


def create_and_display_oval(x, y, x_oval, y_oval, x_size, y_size, corner, color):
    image = Image.new("RGBA", (int(x_oval / cof), int(y_oval / cof)), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, x_oval / cof, y_oval / cof), fill = color)
    rotated_image = image.rotate(corner, expand=True)
    tk_image = ImageTk.PhotoImage(rotated_image)
    offset_x = (x + x_size) / cof - rotated_image.width // 2
    offset_y = (y + y_size) / cof - rotated_image.height // 2
    c.create_image(offset_x, offset_y, anchor=NW, image=tk_image)
    tk_images.append(tk_image)
    return tk_image

def bush_1(x, y, color):
    c.create_polygon((x + 22) / cof, (y + 30) / cof,
                     (x + 25) / cof, (y + 75) / cof,
                     (x + 62) / cof, (y + 119) / cof,
                     (x + 57) / cof, (y + 138) / cof,
                     (x + 77) / cof, (y + 142) / cof,
                     (x + 86) / cof, (y + 190) / cof,
                     (x + 73) / cof, (y + 220) / cof,
                     (x + 94) / cof, (y + 218) / cof,
                     (x + 105) / cof, (y + 262) / cof,
                     (x + 89) / cof, (y + 287) / cof,
                     (x + 129) / cof, (y + 313) / cof,
                     (x + 124) / cof, (y + 325) / cof,
                     (x + 124) / cof, (y + 444) / cof,
                     (x - 125) / cof, (y + 444) / cof,
                     (x - 125) / cof, (y + 324) / cof,
                     (x - 121) / cof, (y + 313) / cof,
                     (x - 85) / cof, (y + 291) / cof,
                     (x - 102) / cof, (y + 258) / cof,
                     (x - 78) / cof, (y + 211) / cof,
                     (x - 89) / cof, (y + 164) / cof,
                     (x - 60) / cof, (y + 129) / cof,
                     (x - 67) / cof, (y + 96) / cof,
                     (x - 27) / cof, (y + 69) / cof,
                     (x - 22) / cof, (y + 30) / cof,
                     fill = color)
    c.create_oval((x - 23) / cof, (y - 1) / cof,
                  (x + 23) / cof, (y + 81) / cof,
                  fill = color, outline = color)
    c.create_oval((x - 5) / cof, (y + 73) / cof,
                  (x + 65) / cof, (y + 143) / cof,
                  fill = color, outline = color)
    c.create_oval((x - 106) / cof, (y + 209) / cof,
                  (x - 36) / cof, (y + 279) / cof,
                  fill = color, outline = color)
    c.create_oval((x + 61) / cof, (y + 286) / cof,
                  (x + 131) / cof, (y + 328) / cof,
                  fill = color, outline = color)
    
    create_and_display_oval(x, y, 70, 42, -92, 313, 12.1, color)
    create_and_display_oval(x, y, 82, 50, 83, 251, 46, color)
    create_and_display_oval(x, y, 82, 52, -39, 98, -61, color)
    create_and_display_oval(x, y, 82, 60, -58, 165, -61, color)
    create_and_display_oval(x, y, 82, 52, 63, 179, 62.1, color)

def bush_2(x, y, color):
    c.create_polygon((x + 13) / cof, (y + 37) / cof,
                     (x + 41) / cof, (y + 114) / cof,
                     (x + 73) / cof, (y + 143) / cof,
                     (x + 66) / cof, (y + 178) / cof,
                     (x + 97) / cof, (y + 205) / cof,
                     (x + 80) / cof, (y + 263) / cof,
                     (x + 99) / cof, (y + 318) / cof,
                     (x + 94) / cof, (y + 330) / cof,
                     (x + 94) / cof, (y + 461) / cof,
                     (x - 127) / cof, (y + 461) / cof,
                     (x - 127) / cof, (y + 330) / cof,
                     (x - 137) / cof, (y + 305) / cof,
                     (x - 141) / cof, (y + 273) / cof,
                     (x - 96) / cof, (y + 243) / cof,
                     (x - 116) / cof, (y + 178) / cof,
                     (x - 71) / cof, (y + 153) / cof,
                     (x - 73) / cof, (y + 125) / cof,
                     (x - 38) / cof, (y + 100) / cof,
                     (x - 23) / cof, (y + 37) / cof,
                     fill = color)
    c.create_oval((x - 26) / cof, (y - 1) / cof,
                  (x + 26) / cof, (y + 129) / cof,
                  fill = color, outline = color)
    
    create_and_display_oval(x, y, 130, 46, -48, 138, -76, color)
    create_and_display_oval(x, y, 130, 46, 48, 148, 68, color)
    create_and_display_oval(x, y, 130, 74, -93, 295, -53, color)
    create_and_display_oval(x, y, 130, 66, -70, 201, -53, color)
    create_and_display_oval(x, y, 130, 56, 56, 224, 53, color)
    create_and_display_oval(x, y, 130, 58, 71, 301, 49, color)

def bush_3(x, y, color):
    c.create_polygon((x - 158) / cof, (y + 291) / cof,
                     (x - 86) / cof, (y + 119) / cof,
                     (x + 86) / cof, (y + 68) / cof,
                     (x + 204) / cof, (y + 287) / cof,
                     fill = color)
    c.create_oval((x - 56) / cof, (y + 1) / cof,
                  (x + 59) / cof, (y + 115) / cof,
                  fill = color, outline = color)
    c.create_oval((x + 29) / cof, (y + 19) / cof,
                  (x + 118) / cof, (y + 107) / cof,
                  fill = color, outline = color)
    def oval(x, y):
        c.create_oval(x / cof, (y - 95) / cof,
                      (x + 95) / cof, y / cof,
                      fill = color, outline = color)
    oval(x - 187, y + 269)
    oval(x - 151, y + 205)
    oval(x + 63, y + 170)
    oval(x + 106, y + 225)
    oval(x - 110, y + 150)


def tree1(x, y, color1, color2):
    c.create_oval((x - 118) / cof, (y - 392) / cof,
                  (x + 131) / cof, (y - 113) / cof,
                  fill = color1, outline = color1)
    c.create_polygon(x / cof, y / cof,
                     (x + 18) / cof, (y - 1) / cof,
                     (x + 6) / cof, (y - 228) / cof,
                     (x - 2) / cof, (y - 227) / cof,
                     fill = color2)
    c.create_arc((x - 54) / cof, (y - 279) / cof,
                 (x + 62) / cof, (y - 141) / cof,
                 start=-90, extent=-90, outline = color2, style="arc", width = 10 / cof)
    c.create_arc((x - 55) / cof, (y - 294) / cof,
                 (x + 63) / cof, (y - 164) / cof,
                 start=-90, extent=75, outline = color2, style="arc", width = 9 / cof)

def tree2(x, y, color1, color2):
    create_and_display_oval(x, y, 254, 202, 20, -180, -108, color1)
    c.create_polygon(x / cof, y / cof,
                     (x + 17) / cof, y / cof,
                     (x + 17) / cof, (y - 137) / cof,
                     (x + 8) / cof, (y - 138) / cof,
                     fill = color2)
    c.create_arc((x - 27) / cof, (y - 193) / cof,
                 (x + 51) / cof, (y - 99) / cof,
                 start=-90, extent=-90, outline = color2, style="arc", width = 9 / cof)
    c.create_arc((x - 26) / cof, (y - 210) / cof,
                 (x + 60) / cof, (y - 90) / cof,
                 start=-90, extent=60, outline = color2, style="arc", width = 10 / cof)

c.create_oval(4666 / cof, 1554 / cof,
              5100 / cof, 1988 / cof,
              fill = '#fefefe', outline = '#fefefe')

c.create_polygon(0 / cof, 3400 / cof,
                 0 / cof, 2600 / cof,
                 1660 / cof, 1604 / cof,
                 2466 / cof, 1880 / cof,
                 3072 / cof, 1484 / cof,
                 4733 / cof, 2049 / cof,
                 5210 / cof, 1662 / cof,
                 5738 / cof, 1885 / cof,
                 6200 / cof, 1553 / cof,
                 6200 / cof, 3400 / cof,
                 fill = '#4e5f6f')

c.create_polygon(0 / cof, 3400 / cof,
                 0 / cof, 1970 / cof,
                 840 / cof, 1500 / cof,
                 1958 / cof, 1940 / cof,
                 2300 / cof, 1740 / cof,
                 3180 / cof, 2010 / cof,
                 3980 / cof, 1500 / cof,
                 5350 / cof, 1944 / cof,
                 5650 / cof, 1740 / cof,
                 6200 / cof, 1963 / cof,
                 6200 / cof, 3400 / cof,
                 fill = '#1c1912')


bush_3(3682, 2066, '#1e2f43')

triangle_1(409, 1962, '#232f47')
triangle_1(552, 2023, '#384b6b')
triangle_1(676, 2073, '#384b6b')
triangle_1(1117, 2012, '#5e7094')
triangle_1(1628, 2113, '#374a6a')
triangle_1(1845, 2063, '#222e46')
triangle_1(1930, 2145, '#394a68')
triangle_1(2292, 2018, '#222e46')
triangle_1(2427, 1961, '#222e46')
triangle_1(2776, 2138, '#394a68')
triangle_1(2973, 2009, '#5e7192')
triangle_1(3277, 2073, '#232f47')
triangle_1(3640, 2022, '#232f47')
triangle_1(4185, 2020, '#374a6a')
triangle_1(4309, 2071, '#374a6a')
triangle_1(4043, 1964, '#232f47')
triangle_1(4751, 2011, '#5d7091')

bush_3(1384, 2161, '#394a68')

bush_1(1514, 2046, '#5d7091')
bush_1(2183, 2096, '#222e46')
bush_1(2027, 2045, '#5c6f90')
bush_1(3567, 2046, '#222e46')
bush_1(5147, 2045, '#607092')
bush_1(3900, 2130, '#485b7c')
    
bush_2(964, 2154, '#3a4b69')
bush_2(807, 2040, '#26364d')
bush_2(1748, 2104, '#222e46')
bush_2(2129, 2199, '#394a68')
bush_2(2550, 2155, '#39496a')

bush_3(2834, 2214, '#232f47')

bush_2(2647, 2199, '#5d7091')
bush_2(3233, 2155, '#5c6f8f')
bush_2(3393, 2039, '#3a4b69')
bush_2(4597, 2154, '#374a68')
bush_2(4441, 2039, '#25354c')

triangle_2(1236, 2166, '#384b6b')
triangle_2(2065, 2167, '#394a68')
triangle_2(3110, 2096, '#394a68')
triangle_2(4870, 2165, '#3a4b69')

bush_3(3725, 2163, '#5e7192')
bush_3(5017, 2152, '#3e4a62')
bush_3(1719, 2215, '#5d7091')


c.create_polygon(0 / cof, 3400 / cof,
0 / cof, 2354 / cof,
6200 / cof, 2354 / cof,
6200 / cof, 3400 / cof,
fill = '#3a7cac')

c.create_oval(3810 / cof, 1602 / cof,
	9670 / cof, 7462 / cof,
	fill = '#f3a600', outline = '#f3a600')

c.create_oval(-7530 / cof, 2005 / cof,
	6470 / cof, 16005 / cof,
	fill = '#ee7500', outline='#ee7500')

c.create_oval(-7530 / cof, 2005 / cof,
	6470 / cof, 16005 / cof,
	fill = '#ee7500', outline='#ee7500')
    
bush_3(35, 2389, '#988924')
triangle_1(1837, 2429, '#4e6a2f')
triangle_1(2054, 2383, '#f6a901')
bush_2(1956, 2423, '#e34627')
bush_3(1592, 2479, '#48632c')
bush_3(1880, 2550, '#f3a600')
bush_1(1723, 2364, '#ef521d')
bush_1(621, 2373, '#877427')
triangle_1(792, 2336, '#e24728')
triangle_1(885, 2387, '#4d692e')
triangle_1(2139, 2458, '#d17127')
bush_1(2236, 2361, '#ed6928')
bush_1(2392, 2414, '#897627')
bush_2(1173, 2472, '#e24728')
bush_2(485, 2507, '#e24728')
bush_2(1017, 2357, '#f6a901')
triangle_1(1327, 2325, '#c66403')
triangle_1(341, 2279, '#f8ac08')
bush_1(230, 2451, '#ee6a29')
triangle_2(2274, 2479, '#998c24')
bush_2(2337, 2514, '#f6a901')
triangle_2(1446, 2479, '#998c24')
bush_3(2513, 2530, '#f5a800')


c.create_polygon(0 / cof, 3400 / cof,
                 0 / cof, 2690 / cof,
                 6200 / cof, 2690 / cof,
                 6200 / cof, 3400 / cof,
                 fill = '#3a7cac')

c.create_oval(-5900 / cof, 2496 / cof,
              4220 / cof, 12616 / cof,
              fill = '#ffa901', outline='#ffa901')

c.create_oval(-4171 / cof, 2336 / cof,
              16449 / cof, 22956 / cof,
              fill = '#fed700', outline = '#fed700')



tree1(147, 3083, '#ef732b', '#94661b')
tree1(5934, 2425, '#e34d2a', '#77221d')
tree1(5767, 3219, '#004528', '#96641d')

tree2(383, 3218, '#e34d2a', '#6a211a')
tree2(1134, 3153, '#8e7c2a', '#573915')
tree2(4331, 2613, '#e34d2a', '#521d0f')





















import numpy as np

def find_t(x, y, h, k, a, b):
    cos_t = (x - h) / a
    sin_t = (y - k) / b

    t = np.arccos(cos_t)
    
    # Корректировка для учета всех четвертей
    if sin_t < 0:
        t = 2 * np.pi - t
    
    return t

def generate_ellipse_points_between(h, k, a, b, t1, t2, num_points=100):
    if t2 < t1: t2 += 2 * np.pi
    
    t = np.linspace(t1, t2, num_points)
    x = h + a * np.cos(t)
    y = k + b * np.sin(t)
    return np.column_stack((x, y))

# Пример использования
h, k = 5888, 6832  # центр эллипса
a, b = 3800, 4521  # полуоси эллипса
num_points = 50  # количество точек

# Точки на эллипсе
point1 = (3415, 3400)
point2 = (5185, 2389)

# Найти углы для точек на эллипсе
t1 = find_t(point1[0], point1[1], h, k, a, b)
t2 = find_t(point2[0], point2[1], h, k, a, b)

# Сгенерировать точки между t1 и t2
points = generate_ellipse_points_between(h, k, a, b, t1, t2, num_points)

# Преобразовать точки в список [x1, y1, x2, y2, x3, y3, ...]
result_list = [coord / cof for point in points.tolist() for coord in point]

# Вывод списка
print(result_list)
c.create_polygon(result_list)


root.mainloop()