from tkinter import *
from tkinter import ttk

class TREEViEW(ttk.Treeview):

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
        
        # master de información en tkinter y tkinter.ttk
        self.insert(parent='', index=0, text='widgets info', iid='id_parent_info', tags=['parent_Info_Item', 'info_item'])
        # primer elemento con dos sub elementos
        self.insert(parent='id_parent_info', index=0, text='tkinter lib', iid='id_parent_tkinter_lib', tags=['parent_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=0, text='Button widget', iid='tkinter.Button', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=1, text='Canvas widget', iid='tkinter.Canvas', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=2, text='Checkbutton widget', iid='tkinter.Checkbutton', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=3, text='Entry widget', iid='tkinter.Entry', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=4, text='Frame widget', iid='tkinter.Frame', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=5, text='Label widget', iid='tkinter.Label', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=6, text='LabelFrame widget', iid='tkinter.LabelFrame', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=7, text='Listbox widget', iid='tkinter.Listbox', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=8, text='Menu widget', iid='tkinter.Menu', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=9, text='Menubutton widget', iid='tkinter.Menubutton', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=10, text='Message widget', iid='tkinter.Message', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=11, text='OptionMenu widget', iid='tkinter.OptionMenu', tags=['special_sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=12, text='PanedWindow widget', iid='tkinter.PanedWindow', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=13, text='Radiobutton widget', iid='tkinter.Radiobutton', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=14, text='Scale widget', iid='tkinter.Scale', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=15, text='Scrollbar widget', iid='tkinter.Scrollbar', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=16, text='Spinbox widget', iid='tkinter.Spinbox', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_lib', index=17, text='Text widget', iid='tkinter.Text', tags=['sub_Info_Item', 'info_item'])

        # segundo elemento con un sub elemento
        self.insert(parent='id_parent_info', index=1, text='tkinter ttk lib', iid='id_parent_tkinter_ttk', tags=['parent_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_ttk', index=0, text='Button widget', iid='ttk.Button', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_ttk', index=1, text='Treeview widget', iid='ttk.Treeview', tags=['sub_Info_Item', 'info_item'])
        self.insert(parent='id_parent_tkinter_ttk', index=2, text='Notebook widget', iid='ttk.Notebook', tags=['sub_Info_Item', 'info_item'])

        # Configuración por tags
        # self.tag_configure(tagname='parent_Info_Item', foreground='red')
        self.tag_configure(tagname='special_sub_Info_Item', foreground='blue')
        # self.tag_configure(tagname='info_item', font={'font':'Arial', 'size':8, 'type':'bold'})


def lounchApp():
    app = Tk()
    treeview = TREEViEW(app)
    treeview.pack(fill='both', expand='true')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass