from tkinter import *
import random, tkinter
from PIL import Image, ImageDraw, ImageTk
import numpy as np
 

root = Tk()
root.title('Drawing Project')

cof = 4
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

def tree3(x, y, color1, color2):
    create_and_display_oval(x, y, 244, 120, -4, -141, 4, color1)
    create_and_display_oval(x, y, 226, 116, -23, -257, 7, color1)
    c.create_oval((x - 68) / cof, (y - 406) / cof,
                  (x + 22) / cof, (y - 274) / cof,
                  fill=color1, outline=color1)
    c.create_polygon((x + 80) / cof, (y - 183) / cof,
                     (x + 56) / cof, (y - 204) / cof,
                     (x + 56) / cof, (y - 217) / cof,
                     (x + 64) / cof, (y - 228) / cof,
                     (x + 45) / cof, (y - 307) / cof,
                     (x + 26) / cof, (y - 319) / cof,
                     (x + 14) / cof, (y - 346) / cof,
                     (x - 24) / cof, (y - 368) / cof,
                     (x - 62) / cof, (y - 348) / cof,
                     (x - 74) / cof, (y - 317) / cof,
                     (x - 101) / cof, (y - 292) / cof,
                     (x - 122) / cof, (y - 239) / cof,
                     (x - 79) / cof, (y - 193) / cof,
                     (x - 103) / cof, (y - 149) / cof,
                     (x - 11) / cof, (y - 115) / cof,
                     fill = color1, smooth = 1)
    c.create_polygon(x / cof, y / cof,
                     (x - 14) / cof, (y - 225) / cof,
                     (x - 7) / cof, (y - 224) / cof,
                     (x + 17) / cof, (y - 1) / cof,
                     fill=color2)
    lst = [[-87, -283, 79, -117, -90, -50, 9],
        [-48, -282, 36, -166, -90, 60, 9],
        [-59, -331, 41, -193, -90, -50, 9],
        [-4, -268, 88, -176, -80, -40, 8]]
    for i in lst:
        c.create_arc((x + i[0]) / cof, (y + i[1]) / cof,
                 (x + i[2]) / cof, (y + i[3]) / cof,
                 start=i[4], extent=i[5], outline = color2, style="arc", width = i[6] / cof)

def tree4(x, y, color1, color2):
    create_and_display_oval(x, y, 238, 152, 3, -138, 7, color1)
    create_and_display_oval(x, y, 178, 102, -53, -196, -36, color1)
    create_and_display_oval(x, y, 130, 74, 23, -225, 39, color1)
    create_and_display_oval(x, y, 120, 76, -15, -281, -85, color1)
    c.create_polygon(x / cof, y / cof,
                     (x - 7) / cof, (y - 191) / cof,
                     (x + 2) / cof, (y - 190) / cof,
                     (x + 15) / cof, (y - 1) / cof,
                     fill=color2)
    lst = [[-56, -224, 60, -108, -90, 50, 9],
           [-86, -297, 82, -129, -90, -60, 9],
           [-119, -227, -1, -139, -100, 30, 8],
           [-44, -255, 42, -151, -90, 75, 8],
           [-34, -246, 30, -182, -90, -60, 8]]
    for i in lst:
        c.create_arc((x + i[0]) / cof, (y + i[1]) / cof,
                 (x + i[2]) / cof, (y + i[3]) / cof,
                 start=i[4], extent=i[5], outline = color2, style="arc", width = i[6] / cof)

def tree5(x, y, color1, color2):
    create_and_display_oval(x, y, 182, 218, 113, -205, -26, color1)
    create_and_display_oval(x, y, 184, 118, -120, -170, -16, color1)





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

tree3(3238, 3276, '#e34d2a', '#4d180a')
tree3(5433, 2544, '#ef7f01', '#743e02')

tree4(4342, 3082, '#ef732b', '#7b3c13')
tree4(5691, 2467, '#fbc725', '#966614')

tree5(3962, 2776, '#8e7c2a', '#4e2b15')


























##########################################################################################################################################################

"""

def branch():
    c.create_polygon(0 / cof, 68 / cof,
        174 / cof, 89 / cof,
        382 / cof, 55 / cof,
        379 / cof, 74 / cof,
        217 / cof, 106 / cof,
        675 / cof, 161 / cof,
        669 / cof, 168 / cof,
        0 / cof, 100 / cof,
        fill = '#000000')

    c.create_polygon(1380 / cof, 0 / cof,
        1401 / cof, 0 / cof,
        1617 / cof, 140 / cof,
        2017 / cof, 177 / cof,
        2013 / cof, 188 / cof,
        1634 / cof, 151 / cof,
        1792 / cof, 252 / cof,
        1787 / cof, 260 / cof,
        fill = '#000000')

    c.create_polygon(0 / cof, 250 / cof,
                    619 / cof, 587 / cof,
                    1212 / cof, 706 / cof,
                    1765 / cof, 666 / cof,
                    1761 / cof, 688 / cof,
                    1224 / cof, 720 / cof,
                    1689 / cof, 932 / cof,
                    1687 / cof, 946 / cof,
                    1674 / cof, 954 / cof,
                    1180 / cof, 715 / cof,
                    665 / cof, 630 / cof,
                    1086 / cof, 915 / cof,
                    1383 / cof, 1015 / cof,
                    1749 / cof, 979 / cof,
                    1609 / cof, 806 / cof,
                    1069 / cof, 336 / cof,
                    1050 / cof, 308 / cof,
                    770 / cof, 2 / cof,
                    763 / cof, 2 / cof,
                    826 / cof, 256 / cof,
                    1219 / cof, 715 / cof,
                    1203 / cof, 713 / cof,
                    830 / cof, 278 / cof,
                    920 / cof, 532 / cof,
                    1020 / cof, 815 / cof,
                    1011 / cof, 821 / cof,
                    944 / cof, 651 / cof,
                    908 / cof, 531 / cof,
                    819 / cof, 280 / cof,
                    737 / cof, 0 / cof,
                    816 / cof, 0 / cof,
                    1062 / cof, 289 / cof,
                    1452 / cof, 415 / cof,
                    1648 / cof, 424 / cof,
                    2021 / cof, 331 / cof,
                    2315 / cof, 284 / cof,
                    2319 / cof, 287 / cof,
                    2318 / cof, 292 / cof,
                    2138 / cof, 320 / cof,
                    2020 / cof, 342 / cof,
                    1634 / cof, 434 / cof,
                    1943 / cof, 452 / cof,
                    2015 / cof, 465 / cof,
                    2373 / cof, 411 / cof,
                    2375 / cof, 418 / cof,
                    2369 / cof, 422 / cof,
                    2041 / cof, 471 / cof,
                    2290 / cof, 600 / cof,
                    2284 / cof, 608 / cof,
                    2025 / cof, 475 / cof,
                    1923 / cof, 469 / cof,
                    1494 / cof, 440 / cof,
                    1724 / cof, 585 / cof,
                    2153 / cof, 776 / cof,
                    2149 / cof, 784 / cof,
                    2142 / cof, 784 / cof,
                    1716 / cof, 595 / cof,
                    1484 / cof, 442 / cof,
                    1097 / cof, 330 / cof,
                    1582 / cof, 750 / cof,
                    2137 / cof, 989 / cof,
                    2139 / cof, 998 / cof,
                    2129 / cof, 1002 / cof,
                    1595 / cof, 769 / cof,
                    1769 / cof, 981 / cof,
                    2006 / cof, 963 / cof,
                    1993 / cof, 974 / cof,
                    1783 / cof, 994 / cof,
                    1872 / cof, 1104 / cof,
                    1864 / cof, 1113 / cof,
                    1766 / cof, 996 / cof,
                    1388 / cof, 1029 / cof,
                    1482 / cof, 1135 / cof,
                    1935 / cof, 1246 / cof,
                    1925 / cof, 1255 / cof,
                    1496 / cof, 1153 / cof,
                    1740 / cof, 1445 / cof,
                    1734 / cof, 1453 / cof,
                    1362 / cof, 1031 / cof,
                    1102 / cof, 947 / cof,
                    595 / cof, 617 / cof,
                    270 / cof, 449 / cof,
                    674 / cof, 1049 / cof,
                    1044 / cof, 1347 / cof,
                    1042 / cof, 1353 / cof,
                    1037 / cof, 1356 / cof,
                    667 / cof, 1062 / cof,
                    784 / cof, 1397 / cof,
                    776 / cof, 1405 / cof,
                    643 / cof, 1028 / cof,
                    199 / cof, 412 / cof,
                    0 / cof, 314 / cof,
                    fill = '#000000')

    c.create_polygon(1193 / cof, 702 / cof,
                    1211 / cof, 705 / cof,
                    1220 / cof, 716 / cof,
                    1201 / cof, 716 / cof,
                    fill = '#000000')

    c.create_polygon(1481 / cof, 689 / cof,
                    1518 / cof, 686 / cof,
                    1542 / cof, 703 / cof,
                    1497 / cof, 706 / cof,
                    fill = '#000000')

    c.create_polygon(908 / cof, 531 / cof,
                    964 / cof, 656 / cof,
                    973 / cof, 681 / cof,
                    954 / cof, 678 / cof,
                    fill = '#000000')






def sheet1(x, y):

    number = 0


    while number < number0:

        cooficent0 = random.randint(1, 5)
        cooficent1 = 0
        if cooficent0 == 1:
            cooficent1 = 0.9
        elif cooficent0 == 2:
            cooficent1 = 0.95
        elif cooficent0 == 3:
            cooficent1 = 1
        elif cooficent0 == 4:
            cooficent1 = 1.05
        elif cooficent0 == 5:
            cooficent1 = 1.1



        num = random.randint(1, 3)

        if num == 1:
            c.create_polygon((x * cooficent1) / cof, (y * cooficent1) / cof,
                            ((x + 13) * cooficent1) / cof, ((y - 3) * cooficent1) / cof,
                            ((x + 26) * cooficent1) / cof, ((y - 7) * cooficent1) / cof,
                            ((x + 61) * cooficent1) / cof, ((y - 12) * cooficent1) / cof,
                            ((x + 52) * cooficent1) / cof, ((y - 18) * cooficent1) / cof,
                            ((x + 59) * cooficent1) / cof, ((y - 10) * cooficent1) / cof,
                            ((x + 66) * cooficent1) / cof, ((y - 1) * cooficent1) / cof,
                            ((x + 75) * cooficent1) / cof, ((y + 7) * cooficent1) / cof,
                            ((x + 100) * cooficent1) / cof, ((y + 26) * cooficent1) / cof,
                            ((x + 93) * cooficent1) / cof, ((y + 36) * cooficent1) / cof,
                            ((x + 85) * cooficent1) / cof, ((y + 44) * cooficent1) / cof,
                            ((x + 76) * cooficent1) / cof, ((y + 49) * cooficent1) / cof,
                            ((x + 65) * cooficent1) / cof, ((y + 53) * cooficent1) / cof,
                            ((x + 49) * cooficent1) / cof, ((y + 54) * cooficent1) / cof,
                            ((x + 48) * cooficent1) / cof, ((y + 36) * cooficent1) / cof,
                            ((x + 42) * cooficent1) / cof, ((y + 41) * cooficent1) / cof,
                            ((x + 39) * cooficent1) / cof, ((y + 48) * cooficent1) / cof,
                            ((x + 34) * cooficent1) / cof, ((y + 49) * cooficent1) / cof,
                            ((x + 27) * cooficent1) / cof, ((y + 46) * cooficent1) / cof,
                            ((x + 20) * cooficent1) / cof, ((y + 40) * cooficent1) / cof,
                            ((x + 12) * cooficent1) / cof, ((y + 33) * cooficent1) / cof,
                            ((x + 5) * cooficent1) / cof, ((y + 23) * cooficent1) / cof,
                            ((x + 1) * cooficent1) / cof, ((y + 15) * cooficent1) / cof,
                            ((x - 2) * cooficent1) / cof, ((y + 6) * cooficent1) / cof,
                            fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1

        elif num == 2:
            c.create_polygon((x * cooficent1) / cof, (y * cooficent1) / cof,
                             ((x + 63) * cooficent1) / cof, ((y - 4) * cooficent1) / cof,
                             ((x + 116) * cooficent1) / cof, ((y + 53) * cooficent1) / cof,
                             ((x + 65) * cooficent1) / cof, ((y + 78) * cooficent1) / cof,
                             ((x + 61) * cooficent1) / cof, ((y + 57) * cooficent1) / cof,
                             ((x + 56) * cooficent1) / cof, ((y + 74) * cooficent1) / cof,
                             ((x + 51) * cooficent1) / cof, ((y + 78) * cooficent1) / cof,
                             ((x + 30) * cooficent1) / cof, ((y + 75) * cooficent1) / cof,
                             ((x + 30) * cooficent1) / cof, ((y + 66) * cooficent1) / cof,
                             ((x + 37) * cooficent1) / cof, ((y + 45) * cooficent1) / cof,
                             ((x + 35) * cooficent1) / cof, ((y + 44) * cooficent1) / cof,
                             ((x + 16) * cooficent1) / cof, (( y + 74) * cooficent1) / cof,
                             ((x + 9) * cooficent1) / cof, ((y + 68) * cooficent1) / cof,
                             ((x + 1) * cooficent1) / cof, ((y + 57) * cooficent1) / cof,
                             ((x - 4) * cooficent1) / cof, ((y + 47) * cooficent1) / cof,
                             ((x - 7) * cooficent1) / cof, ((y + 38) * cooficent1) / cof,
                             ((x - 8) * cooficent1) / cof, ((y + 27) * cooficent1) / cof,
                             ((x - 7) * cooficent1) / cof, ((y + 17) * cooficent1) / cof,
                             fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1


        elif num == 3:
            c.create_polygon((x * cooficent1) / cof, (y * cooficent1) / cof,
                             ((x + 62) * cooficent1) / cof, ((y + 31) * cooficent1) / cof,
                             ((x + 33) * cooficent1) / cof, ((y + 86) * cooficent1) / cof,
                             ((x + 14) * cooficent1) / cof, ((y + 55) * cooficent1) / cof,
                             ((x + 19) * cooficent1) / cof, ((y + 83) * cooficent1) / cof,
                             ((x + 14) * cooficent1) / cof, ((y + 87) * cooficent1) / cof,
                             (x * cooficent1) / cof, ((y + 86) * cooficent1) / cof,
                             ((x - 16) * cooficent1) / cof, ((y + 80) * cooficent1) / cof,
                             ((x - 26) * cooficent1) / cof, ((y + 72) * cooficent1) / cof,
                             ((x - 34) * cooficent1) / cof, ((y + 64) * cooficent1) / cof,
                             ((x - 49) * cooficent1) / cof, ((y + 43) * cooficent1) / cof,
                             ((x - 51) * cooficent1) / cof, ((y + 37) * cooficent1) / cof,
                             ((x - 46) * cooficent1) / cof, ((y + 31) * cooficent1) / cof,
                             ((x - 26) * cooficent1) / cof, ((y + 17) * cooficent1) / cof,
                             fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1






def sheet2(x, y):

    number = 0


    while number < number1:

        cooficent0 = random.randint(1, 5)
        cooficent1 = 0
        if cooficent0 == 1:
            cooficent1 = 0.9
        elif cooficent0 == 2:
            cooficent1 = 0.95
        elif cooficent0 == 3:
            cooficent1 = 1
        elif cooficent0 == 4:
            cooficent1 = 1.05
        elif cooficent0 == 5:
            cooficent1 = 1.1



        num = random.randint(1, 5)

        if num == 1:
            c.create_polygon((x * cooficent1) / cof, (y * cooficent1) / cof,
                             ((x + 67) * cooficent1) / cof, ((y - 41) * cooficent1) / cof,
                             ((x + 157) * cooficent1) / cof, ((y + 11) * cooficent1) / cof,
                             ((x + 87) * cooficent1) / cof, ((y + 55) * cooficent1) / cof,
                             ((x + 78) * cooficent1) / cof, ((y + 26) * cooficent1) / cof,
                             ((x + 52) * cooficent1) / cof, ((y + 48) * cooficent1) / cof,
                             fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1

        elif num == 2:
            c.create_polygon((x * cooficent1) / cof, (y * cooficent1) / cof,
                             ((x + 78) * cooficent1) / cof, ((y - 32) * cooficent1) / cof,
                             ((x + 159) * cooficent1) / cof, ((y + 7) * cooficent1) / cof,
                             ((x + 156) * cooficent1) / cof, ((y + 18) * cooficent1) / cof,
                             ((x + 149) * cooficent1) / cof, ((y + 27) * cooficent1) / cof,
                             ((x + 144) * cooficent1) / cof, ((y + 31) * cooficent1) / cof,
                             ((x + 127) * cooficent1) / cof, ((y + 39) * cooficent1) / cof,
                             ((x + 97) * cooficent1) / cof, ((y + 44) * cooficent1) / cof,
                             ((x + 57) * cooficent1) / cof, ((y + 40) * cooficent1) / cof,
                             ((x + 52) * cooficent1) / cof, ((y + 13) * cooficent1) / cof,
                             ((x + 29) * cooficent1) / cof, ((y + 39) * cooficent1) / cof,
                             fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1

        elif num == 3:
            c.create_polygon(x / cof, y / cof,
                             (x + 66) / cof, (y - 41) / cof,
                             (x + 159) / cof, (y + 11) / cof,
                             (x + 88) / cof, (y + 56) / cof,
                             (x + 79) / cof, (y + 24) / cof,
                             (x + 51) / cof, (y + 47) / cof,
                             fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1

        elif num == 4:
            c.create_polygon((x * cooficent1) / cof, (y * cooficent1) / cof,
                             ((x + 91) * cooficent1) / cof, ((y - 43) * cooficent1) / cof,
                             ((x + 142) * cooficent1) / cof, ((y + 9) * cooficent1) / cof,
                             ((x + 130) * cooficent1) / cof, ((y + 22) * cooficent1) / cof,
                             ((x + 115) * cooficent1) / cof, ((y + 31) * cooficent1) / cof,
                             ((x + 96) * cooficent1) / cof, ((y + 39) * cooficent1) / cof,
                             ((x + 84) * cooficent1) / cof, ((y + 41) * cooficent1) / cof,
                             ((x + 63) * cooficent1) / cof, ((y + 19) * cooficent1) / cof,
                             ((x + 45) * cooficent1) / cof, ((y + 43) * cooficent1) / cof,
                             fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1

        elif num == 5:
            c.create_polygon((x * cooficent1) / cof, (y * cooficent1) / cof,
                             ((x + 116) * cooficent1) / cof, (y * cooficent1) / cof,
                             ((x + 141) * cooficent1) / cof, ((y + 70) * cooficent1) / cof,
                             ((x + 119) * cooficent1) / cof, ((y + 81) * cooficent1) / cof,
                             ((x + 102) * cooficent1) / cof, ((y + 82) * cooficent1) / cof,
                             ((x + 77) * cooficent1) / cof, ((y + 81) * cooficent1) / cof,
                             ((x + 58) * cooficent1) / cof, ((y + 70) * cooficent1) / cof,
                             ((x + 59) * cooficent1) / cof, ((y + 40) * cooficent1) / cof,
                             ((x + 38) * cooficent1) / cof, ((y + 62) * cooficent1) / cof,
                             fill = color)
            x = random.randint(num1, num1_1)
            y = random.randint(num2, num2_2)
            number += 1





c.create_polygon(0 / cof, 0 / cof,
                 2112 / cof, 0 / cof,
                 1574 / cof, 750 / cof,
                 1280 / cof, 758 / cof,
                 1238 / cof, 952 / cof,
                 0 / cof, 1016 / cof,
                 fill = '#ef8e01')



number0 = 300
number1 = 250
num1 = 0
num1_1 = 0
num2 = 0
num2_2 = 0


color = '#ffa901'


num1 = 0
num1_1 = 600
num2 = 0
num2_2 = 1600
number0 = 200
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 600
num1_1 = 1320
num2_2 = 1700
number0 = 320
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 1320
num1_1 = 1520
num2 = 1340
num2_2 = 1555
number0 = 4
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 1320
num1_1 = 1770
num2 = 0
num2_2 = 1340
number0 = 200
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 1770
num1_1 = 2310
num2_2 = 1100
number0 = 185
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 2310
num1_1 = 2450
num2 = 480
num2_2 = 680
number0 = 3
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 2310
num1_1 = 2680
num2 = 0
num2_2 = 480
number0 = 140
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 2680
num1_1 = 2850
num2_2 = 300
number0 = 3
sheet1(random.randint(num1, num1_1), random.randint(num2, num2_2))



branch()



color = '#ffc700'


num1 = 0
num1_1 = 1000
num2_2 = 1520
number1 = 180
sheet2(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 1000
num1_1 = 1640
num2_2 = 1160
number1 = 120
sheet2(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 1640
num1_1 = 2100
num2_2 = 990
number1 = 105
sheet2(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 2100
num1_1 = 2390
num2_2 = 520
number1 = 8
sheet2(random.randint(num1, num1_1), random.randint(num2, num2_2))

num1 = 2390
num1_1 = 2590
num2_2 = 320
number1 = 7
sheet2(random.randint(num1, num1_1), random.randint(num2, num2_2))

"""



root.mainloop()