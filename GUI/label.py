import tkinter

class myGUI:
    def __init__(self):
        self.mainwindow = tkinter.Tk()

        self.Label1 = tkinter.Label(self.mainwindow, text = "Hello World!")
        self.Label2 = tkinter.Label(self.mainwindow, text = "This is my GUI Program")

        self.Label1.pack(side = 'left')
        self.Label2.pack(side = 'bottom')


        tkinter.mainloop()

my_gui = myGUI() #keeps loop open, allowing users to use the specific funcitons until changed by dev or customer

print('I am done')