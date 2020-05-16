from tkinter import *
from tkinter import ttk


class NOTEBOOK(ttk.Notebook):
    '''
        En este demo utilizo el widget Notebook el cual se encuentra en la librería tkinter.ttk
        construido con tres pestañas que contienen un frame cada una el cual puede llevar un titulo.
        Para presentar los modulos que hacen el demo de los widgets, tanto de la librería tkinter
        como de la librería tkinter.ttk, utilizo el widget Treevew que se encuentra en la misma librería

        El módulo tkinter.ttk proporciona acceso al conjunto de widgets temáticos Tk, introducido en Tk 8.5.
        Si Python no se ha compilado contra Tk 8.5, aún se puede acceder a este módulo si se ha instalado Tile.
        El primer método que usa Tk 8.5 proporciona beneficios adicionales, incluida la representación de fuentes suavizadas en X11
        y la transparencia de la ventana (que requiere un administrador de ventanas de composición en X11).

        La idea básica para tkinter.ttk es separar, en la medida de lo posible,
        el código que implementa el comportamiento de un widget del código que implementa su apariencia.

    '''
    def __init__(self, master):

        super().__init__(master)

        self.tkinter_ttk_widgets = []
        # ************    tabs   ****************
        self.first_tab = Frame(self)
        self.second_tab = Frame(self)
        self.therth_tab = Frame(self)
        master.bind('<Configure>', self.getSize)

        # ********* first tab frame content ****************
        self.frameContent_tab_1 = LabelFrame(self.first_tab, labelanchor='n', text='Frame 1', relief='raised')
        self.frameContent_tab_1.config(borderwidth=1, fg='black', bg='lightgrey')

        # ********* second tab frame content ****************
        self.frameContent_tab_2 = LabelFrame(self.second_tab, labelanchor='n', text='Frame 2', relief='raised')
        self.frameContent_tab_2.config(borderwidth=1, fg='black', bg='lightgrey')

        # ********* therth tab frame content ****************
        self.frameContent_tab_3 = LabelFrame(self.therth_tab, labelanchor='n', text='Frame 3', relief='raised')
        self.frameContent_tab_3.config(borderwidth=1, fg='black', bg='lightgrey')

        # ******** first tab text box ************
        self.textbox = Label(self.frameContent_tab_1)
        self.textbox.config(borderwidth=0, fg='black', bg='white', relief='flat', justify='left', text=self.__doc__)
        # print(self.textbox.keys())

        self.add(child=self.first_tab, text='ficha uno')
        self.add(child=self.second_tab, text='ficha dos')
        self.add(child=self.therth_tab, text='ficha tres')

        self.pack(expand=True, fill='both', side='right')
        self.frameContent_tab_1.pack(expand=True, fill='both')
        self.frameContent_tab_2.pack(expand=True, fill='both')
        self.frameContent_tab_3.pack(expand=True, fill='both')

        self.textbox.pack(expand=True, fill='both', side='top')

    def getSize(self, e):
        if e.x != 0 or e.y != 0 :
            pass
        else:
            self.config(width=int(e.width * 0.95))

    def setContentTitle(self, widget, title):
        self.widget = widget
        self.title = title
        self.widget.config(text=self.title)

    def setTabTitle(self, tab_id, title):
        self.tab_id = tab_id
        self.title = title
        self.tab(self.tab_id, text=self.title)

    def infoWidget(self):
        pass

def lounchApp():
    app = Tk()
    notebook = NOTEBOOK(app)
    app.mainloop()

if __name__ == '__main__':
    lounchApp()

else:
    pass