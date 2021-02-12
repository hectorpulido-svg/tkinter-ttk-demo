from tkinter import *
from tkinter import ttk


class NOTEBOOK(ttk.Notebook):
    '''
    Widget Notebook librería tkinter.ttk con tres pestañas

    El módulo tkinter.ttk proporciona acceso al conjunto de widgets temáticos Tk
    El primer método que usa Tk 8.5 proporciona beneficios adicionales
    incluida la representación de fuentes suavizadas en X11 y la transparencia de la ventana
    La idea básica para tkinter.ttk es separar, en la medida de lo posible,
    el código que implementa el comportamiento de un widget del código que implementa su apariencia.

    '''
    def __init__(self, master):

        super().__init__(master)

        self.tkinter_ttk_widgets = []
        # ************    tabs   ****************
        self.demoTab = Frame(self)
        self.infoTab = Frame(self)
        self.codeTab = Frame(self)
        self.demoTab_name = 'pestaña 1'
        self.infoTab_name = 'pestaña 2'
        self.codeTab_name = 'pestaña 3'

        self.add(child=self.demoTab, text=self.demoTab_name)
        self.add(child=self.infoTab, text=self.infoTab_name)
        self.add(child=self.codeTab, text=self.codeTab_name)

    def setTabTitle(self, tab_id, title):
        self.tab_id = tab_id
        self.title = title
        self.tab(self.tab_id, text=self.title)

    def getTabTitle(self):
        return self.demoTab_name

def lounchApp():
    app = Tk()
    notebook = NOTEBOOK(app)
    notebook.pack(fill='both', expand='true')
    # notebook.setTabTitle(notebook.infoTab, 'cambio de texto')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass