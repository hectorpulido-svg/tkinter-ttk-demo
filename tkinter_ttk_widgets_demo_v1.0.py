from tkinter import *
from modulos.treeviewclass import TREEViEW
from modulos.notebookclass import NOTEBOOK


class DEMO(Frame):
    '''
        La ventana principal
    '''
    def __init__(self, master, title=''):

        super().__init__(master)

        # panel horizontal
        self.treeview_panedwindow = PanedWindow(self.master, orient='horizontal')
        self.treeview_panedwindow.config(sashrelief='raised')
        self.treeview_panedwindow.pack(fill='both', expand='true', side='left')

        # contenido del panel horizontal
        self.treeview = TREEViEW(self.treeview_panedwindow)
        self.treeview_panedwindow.add(self.treeview)

        # panel vertical
        self.notebook_panedwindow = PanedWindow(self.master, orient='vertical')
        self.notebook_panedwindow.config(sashrelief='raised')
        self.notebook_panedwindow.pack(fill='both', expand='true', side='right')

        # el panel vertical pertenece al panel horizontal
        # esta linea va antes de el contenido del seguno panel
        self.treeview_panedwindow.add(self.notebook_panedwindow)

        # contenido del panel vertical
        self.notebook = NOTEBOOK(self.notebook_panedwindow)
        self.notebook_panedwindow.add(self.notebook)

        # print(self.treeview.keys())


def lounchApp():
    app = Tk()
    app.title('TKINTER & TTK DEMO')
    app.geometry('800x600')
    demo = DEMO(app)
    app.mainloop()

if __name__ == '__main__':
    lounchApp()
    
