import tkinter
from tkinter import *
# from tkinter import ttk
from modulos.treeviewclass import TREEViEW
from modulos.notebookclass import NOTEBOOK
from modulos.infoboxclass import INFOBOX

# para depuración 
import time


class DEMO(Frame):
    '''
        La ventana principal
    '''

    def __init__(self, master, title=''):

        super().__init__(master)

        # ---------------------------------------
        #               TREEVIEW PANEL
        self.treeview_panel = PanedWindow(self.master, orient='horizontal')
        self.treeview_panel.config(sashrelief='raised', showhandle=True, opaqueresize=False, background='lightgrey')
        self.treeview_panel.pack(fill='both', expand='true', side='left')

        # añade el treeview
        self.treeview = TREEViEW(self.treeview_panel)
        self.treeview_panel.add(self.treeview)

        # ---------------------------------------
        #               NOTEBOOK PANEL
        self.notebook_panel = PanedWindow(self.master, orient='vertical')
        self.notebook_panel.config(sashrelief='raised', showhandle=True, opaqueresize=False)
        self.notebook_panel.pack(fill='both', expand='true', side='top')

        # el notebook_panel pertenece al treeview_panel
        # esta linea va antes de añadir el notebook
        self.treeview_panel.add(self.notebook_panel)

        # añade el notebook
        self.notebook = NOTEBOOK(self.notebook_panel)
        self.notebook_panel.add(self.notebook)

        # ---------------------------------------
        #           EXTRA INFO PANEL
        self.extrainfo_panel = PanedWindow(self.master, orient='vertical')
        self.extrainfo_panel.config(sashrelief='raised')
        self.extrainfo_panel.pack(fill='both', expand='true', side='bottom')

        # el extrainfo_panel pertenece al notebook_panel
        self.notebook_panel.add(self.extrainfo_panel)

        # coloca el overview
        self.extrainfo = INFOBOX(self.extrainfo_panel)
        self.extrainfo_panel.add(self.extrainfo)
        self.currentSubItem = self.treeview.tag_bind(
            tagname='sub_Info_Item', sequence='<<TreeviewSelect>>', callback=self.responseSub_Item)
        self.currentParItem = self.treeview.tag_bind(
            tagname='parent_Info_Item', sequence='<<TreeviewSelect>>', callback=self.responseParent_Item)


    def responseSub_Item(self, e):
        import importlib
        global cls2Binstace, component
        module = self.treeview.selection()[0].split('.')[0]

        if module == 'ttk':
            module = 'tkinter.ttk'

        component = self.treeview.selection()[0].split('.')[1:]

        mod = importlib.import_module(name=module, package=module)
        for cls_name in component:
            cls2Binstace = getattr(mod, cls_name)
            obj = {cls_name: cls2Binstace}

            self.extrainfo.delete('1.0', END)
            self.extrainfo.insert(END, 'Origen : %s \nObjeto : %s \nclase : %s \nComponente : %s' % (
                str(mod), str(obj), cls2Binstace, str(cls_name)))
            self.notebook.overview.delete('1.0', END)

            self.notebook.overview.insert(
                END, 'clase : ' + cls_name + '  ' + 'opciones de configuración (keys)' + '\n\n') # con formato

            self.getkey(list(cls2Binstace().keys()))

            object_methods = [method_name for method_name in dir(cls2Binstace)
                  if callable(getattr(cls2Binstace, method_name))]
            self.notebook.overview.insert(END, '\n\nmetodos de la clase\n\n' + str(object_methods))

            self.notebook.setTabTitle(self.notebook.first_tab, 'opciones de configuración y metodos del widget %s ' % (cls_name) )
            self.notebook.setContentTitle(self.notebook.frameContent_tab_1, str(cls2Binstace))
            
            # TODO
            # self.widgetdemo = Frame(self.notebook.frameContent_tab_2)
            # self.widgetcached = cls2Binstace(self.widgetdemo, text='instancias cachada')
            # self.widgetcached.pack(side='bottom')


    def responseParent_Item(self, e):
        self.notebook.overview.delete('1.0', END)
        self.text_loader(_description)
        self.extrainfo.delete('1.0', END)
        self.extrainfo.insert('1.0',  self.treeview.selection()[0])
        self.notebook.setTabTitle(self.notebook.first_tab, self.notebook.tab_label_1)
        self.notebook.setContentTitle(self.notebook.frameContent_tab_1, 'ventana de bienvenida')

    def getkey(self, elements):
        
        for i, element in enumerate(elements):
            self.notebook.overview.insert(END, elements[i] + '\n')

    def text_loader(self, txt):
        self.notebook.overview.insert('1.0', txt)


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
