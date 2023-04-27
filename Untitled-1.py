from tkinter import *
from tkinter import ttk

# declare the window
window = Tk()
# set window title
window.title("deez")
# set window width and height
window.configure(width=500, height=300)
# set window background color
window.configure(bg='white')
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
window.mainloop()