import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import numpy as np

def plot():
    ax.clear()
    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    ax.scatter(x, y)
    canvas.draw()

# Initialize Tkinter
root = tk.Tk()
fig, ax = plt.subplots()

frame = tk.Frame(root)
label = tk.Label(text = "Matasploit + Tkinter!")
label.config(font=("Courier", 32))
label.pack()

canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().pack()

toolbar = NavigationToolbar2Tk(canvas, frame, pack_toolbar = False)
toolbar.update()
toolbar.pack(anchor="w", fill = tk.X)



frame.pack()

tk.Button(frame, text = "Plot Graph", command= plot).pack(pady = 10)
root.mainloop()