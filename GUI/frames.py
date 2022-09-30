import tkinter

class myGUI:
    def __init__(self):
        self.mainwindow = tkinter.Tk()

        self.mainwindow.geometry('500x200')
        self.mainwindow.title('Label Demo')

        self.topframe = tkinter.Frame(self.mainwindow)
        self.bottomframe = tkinter.Frame(self.mainwindow)

        self.Label1 = tkinter.Label(self.topframe, text = 'John')
        self.Label2 = tkinter.Label(self.topframe, text = 'Jim')
        self.Label3 = tkinter.Label(self.topframe, text = 'Jerry')
        
        self.Label1.pack(side = 'left')
        self.Label2.pack(side = 'left')
        self.Label3.pack(side = 'left')

        self.Label4 = tkinter.Label(self.bottomframe, text = 'Jill')
        self.Label5 = tkinter.Label(self.bottomframe, text = 'Jen')
        self.Label6 = tkinter.Label(self.bottomframe, text = 'Jessica')


        self.Label4.pack(side = 'left')
        self.Label5.pack(side = 'left')
        self.Label6.pack(side = 'left')

        self.mybutton = tkinter.Button(self.mainwindow, text = 'Click Me!', command = self.do_something)
        self.quitbutton = tkinter.Button(self.mainwindow, text = 'Quit', command = self.mainwindow.destroy)

        self.topframe.pack()
        self.bottomframe.pack()

        self.mybutton.pack(side = 'left')
        self.quitbutton.pack(side = 'right')

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for Clicking me')

my_gui = myGUI() #keeps loop open, allowing users to use the specific funcitons until changed by dev or customer

print('I am done')