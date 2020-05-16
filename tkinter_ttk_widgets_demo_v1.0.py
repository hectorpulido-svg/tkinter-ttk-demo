from tkinter import *
from modulos.treeviewclass import TREEViEW
from modulos.notebookclass import NOTEBOOK


class APP(Tk):
    '''
        La ventana principal
    '''
    def __init__(self, title=''):

        super().__init__()
        self.title(title)
        self.geometry('800x600')
        self.notebook = NOTEBOOK(self)
        self.treevew = TREEViEW(self)

def lounchApp():
    app = APP('TKINTER & TTK DEMO')
    app.mainloop()

if __name__ == '__main__':
    lounchApp()
    
