from tkinter import *
from tkinter import ttk
# from treeviewElements import LOADJSONDOC
import sys
import os
# cwd = os.path.abspath(os.sys.path[0])
# print(cwd)
class METHTREEVIEW(ttk.Treeview):
    '''
    Árbol de modulos

    '''

    def __init__(self, master):
        super().__init__(master)
        self.elements = []
        self.style = ttk.Style()
        self.font = {'font':'Arial', 'size':12, 'type':'bold'}
        self.style.configure("Treeview", foreground='black', background='lightgrey', font=(self.font['font'], self.font['size'], self.font['type']))
        self.style.configure("Treeview.Heading", foreground='black', background='lightgrey', font=(self.font['font'], self.font['size'], self.font['type']))
        self.style.configure("TkHeadingBackground", background='lightgrey')
        self.config(selectmode='browse', style='Treeview')

        # encabezados)
        self.heading('#0', text='Arbol de Metodos')

    def loadElements(self):
        for indx, element in enumerate(self.elements):
            self.insert(parent='', index=0, text=element, iid=element, tags=['method'])

        self.tag_configure(tagname='method', foreground='blue')


def lounchApp():
    app = Tk()
    treeview = METHTREEVIEW(app)
    treeview.elements = ['uno', 'dos', 'tres', 'cuatro']
    treeview.loadElements()
    treeview.pack(fill='both', expand='true')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()