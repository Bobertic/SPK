from tkinter import *
import random, tkinter
from PIL import Image, ImageDraw, ImageTk
import numpy as np

root = Tk()
root.title('Drawing Project')

cof = 5
tk_images = []

c = Canvas(root, width=6200 / cof, height=3400 / cof, bg='#fed48c')
c.pack()



lst = [[[np.float64(5891.814807882953), np.float64(1752.7977672507188)], [np.float64(5997.21353459454), np.float64(1822.92097565958)], [np.float64(6097.952570833623), np.float64(1899.5878037379455)], [np.float64(6193.626276056479), np.float64(1982.4895412282215)]], [[np.float64(5868.10486897366), np.float64(1771.866427857779)], [np.float64(5933.8007670517845), np.float64(1815.5748036254074)], [np.float64(5996.592241519604), np.float64(1863.3618716532005)], [np.float64(6056.226453271294), np.float64(1915.0352102843576)], [np.float64(6112.463276383654), np.float64(1970.3867492219938)], [np.float64(6165.076265018449), np.float64(2029.1936073547881)]]]

c.create_polygon(lst)
root.mainloop()