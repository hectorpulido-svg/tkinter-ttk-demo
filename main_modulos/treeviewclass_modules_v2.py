from tkinter import *
from tkinter import ttk
# from treeviewElements import LOADJSONDOC
import sys
import os
# cwd = os.path.abspath(os.sys.path[0])
# print(cwd)
class MODTREEVIEW(ttk.Treeview):
    '''
    Árbol de modulos

    '''

    def __init__(self, master):
        super().__init__(master)

        self.style = ttk.Style()
        self.font = {'font':'Arial', 'size':12, 'type':'bold'}
        self.style.configure("Treeview", foreground='black', background='lightgrey', font=(self.font['font'], self.font['size'], self.font['type']))
        self.style.configure("Treeview.Heading", foreground='black', background='lightgrey', font=(self.font['font'], self.font['size'], self.font['type']))
        self.style.configure("TkHeadingBackground", background='lightgrey')
        self.config(selectmode='browse', style='Treeview')

        # encabezados)
        self.heading('#0', text='Arbol de Modulos')

        self.loadTreeElements = LOADJSONDOC()
        self.loadTreeElements.readDoc(os.path.join(cwd, 'treeviewElements.json'))
        self.parents = self.loadTreeElements.loadParents()
        self.childs = self.loadTreeElements.loadChilds()

        for pi, self.parent in enumerate(self.parents):
            self.insert(parent=self.parent['parent'], index=self.parent['index'], text=self.parent['text'], iid=self.parent['iid'], tags=self.parent['tags'])
            for self.child in self.childs[pi]:
                self.insert(parent=self.child['parent'], index=self.child['index'], text=self.child['text'], iid=self.child['iid'], tags=self.child['tags'])

        # Configuración por tags
        # self.tag_configure(tagname='parent_item', foreground='red')
        self.tag_configure(tagname='special_child_item', foreground='blue')
        # self.tag_configure(tagname='info_item', font={'font':'Arial', 'size':8, 'type':'bold'})


def lounchApp():
    app = Tk()
    treeview = MODTREEVIEW(app)
    treeview.pack(fill='both', expand='true')
    app.mainloop()

if __name__ == '__main__':
    from treeviewElements import LOADJSONDOC
    cwd = os.path.abspath(os.sys.path[0])
    lounchApp()

else:
    from main_modulos.treeviewElements import LOADJSONDOC
    cwd = os.path.join(os.path.abspath(os.sys.path[0]), 'main_modulos')