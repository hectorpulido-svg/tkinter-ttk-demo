# -*- coding: utf-8 -*-
#!usr/bin/python3

import tkinter
from tkinter import *
from main_modulos.treeviewclass import TREEVIEW
from main_modulos.notebookclass import NOTEBOOK


class DEMO(Frame):
    '''
        La ventana principal
    '''

    def __init__(self, master, title=''):
        super().__init__(master)

        # ---------------------------------------
        #               MENU BAR
        self.menubar = Menu(master)

        self.menu = Menu(self.menubar, tearoff=0)
        self.menu.add_command(label='Abrir', command='')
        self.menu.add_separator()
        self.menu.add_command(label='Salir', command=self.exit)

        self.menubar.add_cascade(label='Archivo', menu=self.menu)

        master.config(menu=self.menubar)
        # ---------------------------------------
        #               TREEVIEW PANEL
        self.treeview_panel = PanedWindow(self.master, orient='horizontal')
        self.treeview_panel.config(
            sashrelief='raised', showhandle=True, opaqueresize=False, background='lightgrey')
        self.treeview_panel.pack(fill='both', expand='true', side='left')

        # añade el treeview
        self.treeview = TREEVIEW(self.treeview_panel)
        self.treeview_panel.add(self.treeview)

        # ---------------------------------------
        #               NOTEBOOK PANEL
        self.notebook_panel = PanedWindow(self.master, orient='vertical')
        self.notebook_panel.config(
            sashrelief='raised', showhandle=True, opaqueresize=False)
        self.notebook_panel.pack(fill='both', expand='true', side='top')

        # el notebook_panel pertenece al treeview_panel
        # esta linea va antes de añadir el notebook
        self.treeview_panel.add(self.notebook_panel)

        # añade el notebook
        self.notebook = NOTEBOOK(self.notebook_panel)
        self.notebook_panel.add(self.notebook)

        # ---------------------------------------
        #           EXTRA INFO PANEL
        self.tips_panel = PanedWindow(self.master, orient='vertical')
        self.tips_panel.config(sashrelief='raised')
        self.tips_panel.pack(fill='both', expand='true', side='bottom')

        # el tips_panel pertenece al notebook_panel
        self.notebook_panel.add(self.tips_panel)

        # coloca el overview
        self.tips = Text(self.tips_panel)
        self.tips.config(borderwidth=2, fg='black', bg='lightgrey')
        self.tips_panel.add(self.tips, height=150, minsize=150)
        
        # eventos
        self.treeview.tag_bind(tagname='parent_item', sequence='<<TreeviewSelect>>', callback=self.onParent_Item)
        self.treeview.tag_bind(tagname='child_item', sequence='<<TreeviewSelect>>', callback=self.onchild_item)
        self.treeview.tag_bind(tagname='test', sequence='<ButtonRelease>', callback=self.showwidgetdemo)

        self.demoState = False

    def onParent_Item(self, e):
        self.notebook.overview.delete('1.0', END)
        self.text_loader(_description)
        self.tips.delete('1.0', END)
        self.tips.insert('1.0',  self.treeview.selection()[0])
        self.notebook.setTabTitle(
            self.notebook.first_tab, self.notebook.tab_label_1)
        self.notebook.setContentTitle(
            self.notebook.infoTab, 'ventana de bienvenida')

        self.cleanDemoTab()

    def onchild_item(self, e):

        self.selection = self.treeview.selection()[0].split('.')

        if len(self.selection) == 3:
            self.package = self.selection[0]
            self.module = self.selection[1]
            self.component = self.selection[2:]
            self.module = self.package + '.' + self.module
        if len(self.selection) == 2:
            self.module = self.selection[0]
            self.component = self.selection[1:]

        self.modImport()

    def modImport(self):

        import importlib
        global cls2Binstance, component, cls_name
        mod = importlib.import_module(name=self.module, package=self.module)
    
        for cls_name in self.component:
            cls2Binstance = getattr(mod, cls_name)
            obj = {cls_name: cls2Binstance}

        self.notebook.overview.delete('1.0', END)
        # ------------- fin de la carga --------------------------------------
        self.tips.delete('1.0', END)
        self.tips.insert(
            END, 'Origen : %s \nObjeto : %s, \nComponente : %s,' % (
            str(mod), str(obj) , str(cls_name)))
    
    def showwidgetdemo(self, e):
        '''
            Presenta un ejemplo de clase
        '''
        self.cleanDemoTab()

        if ('ttk.Tk' in str(cls2Binstance)) or ('tkinter.Tk' in str(cls2Binstance)):
            self.widgetdemo = cls2Binstance()
        else:
            self.widgetdemo = cls2Binstance(self.notebook.demoTab)

        self.getkey(self.widgetdemo.keys())
        self.notebook.setTabTitle(self.notebook.first_tab, 'opciones de configuración y metodos del widget %s ' % (cls_name))
        self.notebook.setContentTitle(self.notebook.infoTab, str(cls2Binstance))
        try:
            self.widgetdemo.pack()
        except:
            pass

        self.demoState = True
    
    def cleanDemoTab(self):
        
        if self.demoState:
            self.widgetdemo.destroy()
            self.demoSate = False
            
    def getkey(self, elements):
        num_elements = len(elements)
        columns = 5
        rows = int(num_elements / columns)
        indx = 0
        self.notebook.overview.insert(
            '1.end', 'clase : ' + cls_name + '  ' + 'opciones de configuración (keys)' + '\n\n')

        for indx, element in enumerate(elements):

            self.notebook.overview.insert(
                self.notebook.overview.index(INSERT), element + ', ')

        object_methods = [method_name for method_name in dir(cls2Binstance)if callable(getattr(cls2Binstance, method_name))]
        self.notebook.overview.insert(
            END, '\n\n metodos de la clase\n\n' + str(object_methods) + '\n')

    def text_loader(self, txt):
        self.notebook.overview.insert('1.0', txt)
    
    def exit(self):
        self.quit()

_description = "En este demo utilizo el widget Notebook el cual se encuentra en la librería tkinter.ttk "\
    "construido con tres pestañas que contienen un frame cada una el cual puede llevar un titulo.\n"\
    "Para presentar los modulos que hacen el demo de los widgets, tanto de la librería tkinter "\
    "como de la librería tkinter.ttk, utilizo el widget Treevew que se encuentra en la misma librería\n"\
    "El módulo tkinter.ttk proporciona acceso al conjunto de widgets temáticos Tk, introducido en Tk 8.5. "\
    "Si Python no se ha compilado contra Tk 8.5, aún se puede acceder a este módulo si se ha instalado Tile.\n"\
    "El primer método que usa Tk 8.5 proporciona beneficios adicionales, incluida la representación de fuentes suavizadas en X11 "\
    "y la transparencia de la ventana (que requiere un administrador de ventanas de composición en X11).\n"\
    "La idea básica para tkinter.ttk es separar, en la medida de lo posible, "\
    "el código que implementa el comportamiento de un widget del código que implementa su apariencia.\n\n "\

def lounchApp():
    app = Tk()
    app.title('TKINTER & TTK DEMO')
    width = '1100'
    height = '600'
    app.geometry(width + 'x' + height)
    demo = DEMO(app)
    demo.text_loader(_description)
    app.mainloop()

if __name__ == '__main__':
    lounchApp()
