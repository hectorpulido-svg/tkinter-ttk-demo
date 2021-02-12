# -*coding: utf-8 -*-
from tkinter import LabelFrame, Label, PhotoImage, StringVar, Button
import os
import sys

class CBUTTON(LabelFrame):
    '''
        Widget de clase Boton con texto en sus extremos depende de imagenes externas
    '''

    def __init__(self, master, Ltext='true', Rtext='false', command=None):
        super().__init__(master)
        self.LT = Ltext
        self.RT = Rtext
        self.Rtext = StringVar()
        self.Ltext = StringVar()
        self.command = command
        self.state = False
        self.config(bg='black', padx=2, pady=5)
        self.imagePath = StringVar()
        self.imagePath.set(btnoffimg)
        self.button = Button(self)
        self.button.config(cursor='hand2', bg='black')
        self.button.bind('<Button-1>', self.onClick)
        self.button.bind('<ButtonRelease-1>', self.onRelease)
        self.button.grid(row=0, column=1)
        self.leftTextlabel = Label(self)
        self.leftTextlabel.config(bg='black', fg='white')
        self.leftTextlabel.grid(row=0, column=0)
        self.rightTextlabel = Label(self)
        self.rightTextlabel.config(bg='black', fg='white')
        self.rightTextlabel.grid(row=0, column=2)
        self.flag = Label(self)
        self.flag.config(bg='green', width=15)
        self.flag.grid(row=1, column=0, columnspan=3)
        self.updatebutton()
        self.swapState = (lambda x: (x==False))
        self.swapImage = (lambda x: (btnoffimg) if x else (btnonimg))
        self.swapFlag = (lambda x: ('red') if x else ('green'))

    def _keys(self):
        return self.button.keys()

    def doc(self):
        return self.__doc__

    def onClick(self, event):
        '''
            actualiza el estado del boton
        '''
        self.imagePath.set((self.swapImage)(self.state))
        self.state = self.swapState(self.state)
        self.flagColor = self.swapFlag(self.state)
        self.flag.config(bg=self.flagColor)

        self.updatebutton()

    def onRelease(self, event):
        '''
            ejecuta la acción
            dada por la instancia de clase
            en el parametro command al soltar el click
        '''
        if self.command is not None:
            self.command()

    def updatebutton(self):
        '''
            actualiza la imagen del boton
        '''
        self.Ltext.set(self.LT)
        self.Rtext.set(self.RT)
        self.rightTextlabel.config(textvariable=self.Rtext)
        self.leftTextlabel.config(textvariable=self.Ltext)
        self.btn_image = PhotoImage(file = self.imagePath.get())
        self.button.config(image=self.btn_image, activebackground='black', highlightbackground='black', relief='flat', bd=0)

if __name__ == '__main__':
    '''
        **********************************************************
               Aquí se implementa una muestra del objeto
        **********************************************************
    '''
    from tkinter import Tk
    app = Tk()
    app.config(bg='black')
    cd = os.path.abspath(sys.path[0])
    btnoffimg = os.path.join(cd, 'img/red/BTN_OFF.png')
    btnonimg = os.path.join(cd, 'img/red/BTN_ON.png')
    test_btn = CBUTTON(app, command=None)
    test_btn.grid(row=0, column=0, columnspan=2)
    print(test_btn.doc())
    app.mainloop()

else:
    '''
        modulo btn.py
    '''
    cd = os.path.abspath(sys.path[0])
    btnoffimg = os.path.join(cd, 'main_modulos/img/red/BTN_OFF.png')
    btnonimg = os.path.join(cd, 'main_modulos/img/red/BTN_ON.png')