import tkinter as tk
from PIL import ImageTk,Image

window = tk.Tk()

img_load = Image.open('bag.png')
img = ImageTk.PhotoImage(img_load)
label = tk.Label(image = img)


def change():
    im = Image.open('rock.png')
    im = ImageTk.PhotoImage(im)
    label.config(image = im)

button = tk.Button(text = 'change',command = change)
button.pack()
label.pack()

window.mainloop()
