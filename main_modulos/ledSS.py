# -*- coding: utf-8 -*-
# usr/bin/python3


from tkinter import LabelFrame, StringVar, Button, Label

class DISPLAY(LabelFrame):
    '''
        Etiqueta.
    ''' 

    def __init__(self, master, string= 'hector miguel pulido garcia' ):
        super().__init__(master)
        self.text = StringVar()
        self.text.set(string.upper())
        self.width = len(self.text.get()) + 6
        self.label = Label(self)
        self.label.config(textvariable=self.text, font={'size':20}, bg='black', fg='red', padx=10, pady=10, width=self.width)
        self.label.pack()
        self.btn = Button(self, text='click to play', command=self.play)
        self.btn.pack()
        self.ledSS = LEDSS(string=self.text.get())
        self._description = 'text de prueba en descripción'

    def play(self):
        self.text.set(self.ledSS.roll())
        self.label.config(textvariable=self.text, padx=10, pady=10, width=self.width)
        self.btn.config(state='disabled')
        self.after(round(3000 / len(self.text.get())), self.play)

    def _keys(self):
        return {'None': None}

    def doc(self):
        return self.ledSS.__doc__


class LEDSS:
    '''
        simula pantalla de led.
    ''' 

    def __init__(self, string=''):
        self.string = StringVar()
        self.string.set(string.rjust(len(string) + 5, chr(32)))
        self.output = StringVar()
        self.output.set(self.string.get())

    def roll(self):
        outGoingCharacter = self.string.get()[0]
        displayedCharacters = self.string.get()[1:len(self.string.get()) - 1]
        inComingCharacters = self.string.get()[len(self.string.get()) - 1:len(self.string.get())] + outGoingCharacter
        self.string.set(displayedCharacters + inComingCharacters)
        self.output.set(displayedCharacters + inComingCharacters[0])
        return self.output.get()

if __name__ == '__main__':

    from tkinter import Tk
    app = Tk()
    testLabel = DISPLAY(app)
    testLabel.grid(row=0, column=0, columnspan=3)
    app.mainloop()