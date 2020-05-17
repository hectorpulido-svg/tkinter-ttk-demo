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
        self.insert(parent='', index=0, text='tkinter lib', iid='id_parent_tkinter_lib', tags='parent_Item')
        self.insert(parent='id_parent_tkinter_lib', index=0, text='Entry widget', iid='tkinter.Entry', tags='sub_Item')
        self.insert(parent='id_parent_tkinter_lib', index=1, text='Button widget', iid='tkinter.Button', tags='sub_Item')

        # segundo elemento con un sub elemento
        self.insert(parent='', index=1, text='tkinter ttk lib', iid='id_parent_tkinter_ttk', tags='parent_Item')
        self.insert(parent='id_parent_tkinter_ttk', index=0, text='Button widget', iid='ttk.Button', tags='sub_Item')

        # tercer elemento con un sub elemento
        self.insert(parent='', index=2, text='wxPython lib', iid='id_parent_wxpython', tags='parent_Item')
        self.insert(parent='id_parent_wxpython', index=0, text='Button widget', iid='wx.Button', tags='sub_Item')

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