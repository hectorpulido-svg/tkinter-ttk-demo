from tkinter import *
from tkinter import ttk

class TREEViEW(ttk.Treeview):

    def __init__(self, master):

        super().__init__(master)
        self.pack(expand=True, fill='both', side='left')


def lounchApp():
    app = Tk()
    treeview = TREEViEW(app)
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass