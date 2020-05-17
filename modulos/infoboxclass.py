from tkinter import *


class INFOBOX(Text):

    def __init__(self, master):

        super().__init__(master)
        self.config(borderwidth=2, fg='black', bg='lightgrey', height=10)
        # print(self.keys())

if __name__ == '__main__':
    test = Tk()
    test_textbox = INFOBOX(test)
    test_textbox.pack(fill='both', expand='true')
    test.mainloop()