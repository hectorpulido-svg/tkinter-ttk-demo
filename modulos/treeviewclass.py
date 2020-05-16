from tkinter import *
from tkinter import ttk

class TREEViEW(ttk.Treeview):

    def __init__(self, master):

        super().__init__(master)
        self.config(selectmode='browse')
        self.heading('#0', text='Arbol de Modulos')
        self.insert('', 0, text='Item_1', iid='id_Item_1', values='valor del item_1')
        self.insert('id_Item_1', 0, text='SubItem_1.1', iid='id_SubItem_1.1')
        self.insert('', 1, text='Item_2', iid='id_Item_2')
        self.insert('id_Item_2', 0, text='SubItem_1.2', iid='id_SubItem_1.2')
        self.bind('<Button-1>', self.infoSelection)

    def infoSelection(self, e):
        print(self.selection())


def lounchApp():
    app = Tk()
    treeview = TREEViEW(app)
    treeview.pack(fill='both', expand='true')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass