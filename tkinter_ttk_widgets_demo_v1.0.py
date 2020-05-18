import tkinter
from tkinter import *
# from tkinter import ttk
from modulos.treeviewclass import TREEViEW
from modulos.notebookclass import NOTEBOOK
from modulos.infoboxclass import INFOBOX


class DEMO(Frame):
    '''
        La ventana principal
    '''

    def __init__(self, master, title=''):

        super().__init__(master)

        # panel del treeview
        self.treeview_panel = PanedWindow(self.master, orient='horizontal')
        self.treeview_panel.config(sashrelief='raised')
        self.treeview_panel.pack(fill='both', expand='true', side='left')

        # coloca treeview
        self.treeview = TREEViEW(self.treeview_panel)
        self.treeview_panel.add(self.treeview)

        # panel del notebook
        self.notebook_panel = PanedWindow(self.master, orient='vertical')
        self.notebook_panel.config(sashrelief='raised')
        self.notebook_panel.pack(fill='both', expand='true', side='top')

        # el panel del notebook pertenece al panel del treeview
        # esta linea va antes de colocar el notebook en su panel
        self.treeview_panel.add(self.notebook_panel)

        # coloca el notebook
        self.notebook = NOTEBOOK(self.notebook_panel)
        self.notebook_panel.add(self.notebook, height=450)

        # panel de informacion
        self.extrainfo_textbox_panel = PanedWindow(
            self.master, orient='vertical')
        self.extrainfo_textbox_panel.config(sashrelief='raised')
        self.extrainfo_textbox_panel.pack(
            fill='both', expand='true', side='bottom')

        # el panel del info pertenece al panel del treeview
        # esta linea va antes de colocar el notebook en su panel
        self.notebook_panel.add(self.extrainfo_textbox_panel)

        # coloca el overview_textbox
        self.extrainfo_textbox = INFOBOX(self.extrainfo_textbox_panel)
        self.extrainfo_textbox_panel.add(self.extrainfo_textbox)
        self.currentSubItem = self.treeview.tag_bind(
            tagname='sub_Item', sequence='<<TreeviewSelect>>', callback=self.responseSubItem)
        self.currentParItem = self.treeview.tag_bind(
            tagname='parent_Item', sequence='<<TreeviewSelect>>', callback=self.responseParItem)

    def responseSubItem(self, e):
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

            self.extrainfo_textbox.delete('1.0', END)
            self.extrainfo_textbox.insert(END, 'Origen : %s \nObjeto : %s \nclase : %s \nComponente : %s' % (
                str(mod), str(obj), cls2Binstace, str(cls_name)))
            self.notebook.overview_textbox.delete('1.0', END)
            self.notebook.overview_textbox.insert(
                END, 'clase : ' + cls_name + '  ' + 'keys' + '\n\n' + str(cls2Binstace().keys()))
            self.widgetcached = cls2Binstace(self.notebook.overview_textbox, text='instancias cachada')
            self.widgetcached.pack(side='bottom')


    def responseParItem(self, e):
        self.notebook.overview_textbox.delete('1.0', END)
        self.overView(_overView)
        self.extrainfo_textbox.delete('1.0', END)
        self.extrainfo_textbox.insert('1.0',  self.treeview.selection()[0])

    def overView(self, txt):
        self.notebook.overview_textbox.insert('1.0', txt)


_overView = "En este demo utilizo el widget Notebook el cual se encuentra en la librería tkinter.ttk "\
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
    demo.overView(_overView)
    app.mainloop()


if __name__ == '__main__':
    lounchApp()
