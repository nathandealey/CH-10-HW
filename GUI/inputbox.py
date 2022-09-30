import tkinter

class myGUI:
    def __init__(self):
        self.mainwindow = tkinter.Tk()

        self.mainwindow.geometry('500x200')
        self.mainwindow.title('Label Demo')

        self.topframe = tkinter.Frame(self.mainwindow)
        self.bottomframe = tkinter.Frame(self.mainwindow)

        self.promptlabel = tkinter.Label(self.topframe, text = 'Enter a distance in Kilometers')
        self.entry = tkinter.Label(self.topframe, width = 10)
        
        self.promptlabel.pack(side = 'left')
        self.entry.pack(side = 'left')


        self.mybutton = tkinter.Button(self.mainwindow, text = 'Convert', command = self.convert)
        self.quitbutton = tkinter.Button(self.mainwindow, text = 'Quit', command = self.mainwindow.destroy)

        self.topframe.pack()
        self.bottomframe.pack()

        self.mybutton.pack(side = 'left')
        self.quitbutton.pack(side = 'right')

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.entry.get())

        miles = round(kilo*0.6124, 2)
        tkinter.messagebox.showinfo('Result', str(kilo) + 'Kilometers is equal to' + str(miles) + 'miles')

my_gui = myGUI() #keeps loop open, allowing users to use the specific funcitons until changed by dev or customer

print('I am done')