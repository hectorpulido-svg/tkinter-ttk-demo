from tkinter import *
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
        self.notebook_panel.add(self.notebook, height=500)

        # panel de informacion
        self.text_panel = PanedWindow(self.master, orient='vertical')
        self.text_panel.config(sashrelief='raised')
        self.text_panel.pack(fill='both', expand='true', side='bottom')

        # el panel del info pertenece al panel del treeview
        # esta linea va antes de colocar el notebook en su panel
        self.notebook_panel.add(self.text_panel)

        # coloca el textbox
        self.text = INFOBOX(self.text_panel)
        self.text_panel.add(self.text)
        # print(self.text_panel.keys())


def lounchApp():
    app = Tk()
    app.title('TKINTER & TTK DEMO')
    width = '1000'
    height = '600'
    app.geometry(width + 'x' + height)
    demo = DEMO(app)
    app.mainloop()

if __name__ == '__main__':
    lounchApp()
    
