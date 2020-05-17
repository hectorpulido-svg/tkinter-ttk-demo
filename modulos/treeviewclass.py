from tkinter import *
from tkinter import ttk

class TREEViEW(ttk.Treeview):

    def __init__(self, master):

        super().__init__(master)

        # modos de selección None|browse:solo uno|extended:varios(establecida por defecto)
        self.config(selectmode='browse')

        # encabezados)
        self.heading('#0', text='Arbol de Modulos')

        # primer elemento con dos sub elementos
        self.insert(parent='', index=0, text='tkinter lib', iid='id_tkinter_lib', tags='parent_Item')
        self.insert(parent='id_tkinter_lib', index=0, text='SubItem_1.1', iid='id_SubItem_1.1', tags='sub_Item')
        self.insert(parent='id_tkinter_lib', index=1, text='Button widget', iid='tkinter.Button', tags='sub_Item')

        # segundo elemento con un sub elemento
        self.insert(parent='', index=1, text='Item_2', iid='id_parent_Item_2', tags='parent_Item')
        self.insert(parent='id_parent_Item_2', index=0, text='SubItem_1.2', iid='id_SubItem_1.2', tags='sub_Item')

        # Configuración por tags
        self.tag_configure(tagname='parent_Item', foreground='red')


def lounchApp():
    app = Tk()
    treeview = TREEViEW(app)
    treeview.pack(fill='both', expand='true')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass