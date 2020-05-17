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
        self.insert(parent='', index=0, text='Item_1', iid='id_parent_Item_1', tags='parent_Item')
        self.insert(parent='id_parent_Item_1', index=0, text='SubItem_1.1', iid='id_SubItem_1.1', tags='sub_Item')
        self.insert(parent='id_parent_Item_1', index=1, text='SubItem_2.1', iid='id_SubItem_2.1', tags='sub_Item')

        # segundo elemento con un sub elemento
        self.insert(parent='', index=1, text='Item_2', iid='id_parent_Item_2', tags='parent_Item')
        self.insert(parent='id_parent_Item_2', index=0, text='SubItem_1.2', iid='id_SubItem_1.2', tags='sub_Item')

        # Eventos por tags
        self.tag_bind(tagname='parent_Item', sequence='<<TreeviewSelect>>', callback=self.selectedItemID)
        # self.tag_bind(tagname='sub_Item', sequence='<<TreeviewSelect>>', callback=self.selectedItemID)

        # Configuración por tags
        self.tag_configure(tagname='parent_Item', foreground='red')


    def selectedItemID(self, e):
        # un metodo de prueba
        s = (lambda x: ('Elemento padre : ' + x) if 'paren' in x else ('Elemento hijo : ' + x))
        print(s(self.selection()[0]))



def lounchApp():
    app = Tk()
    treeview = TREEViEW(app)
    treeview.pack(fill='both', expand='true')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass