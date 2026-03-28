#  -*- coding: utf-8 -*-
# !usr/bin/env python 3

# -------------------------------
# Un simple boton de tkinter

from tkinter import Button, Label, Tk, mainloop

class BUTTON(Button):
    '''
    Boton ejemplo con tkinter
    '''

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(text='click', width=15, padx=10, pady=8, command=self.swap)
        self.swap = (lambda x: 'click' if x=='click again' else 'click again')

    def swap(self):
        '''lambda function to exchange the text'''
        self.config(text=self.swap(self['text']))

if __name__ == '__main__':
    app = Tk()
    b = BUTTON(app)
    b.pack()
    app.mainloop()

