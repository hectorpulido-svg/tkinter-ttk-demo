from tkinter import *
from tkinter import ttk

class TREEViEW(ttk.Treeview):

    def __init__(self, master):

        super().__init__(master)


def lounchApp():
    app = Tk()
    treeview = TREEViEW(app)
    treeview.pack(fill='both', expand='true')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass