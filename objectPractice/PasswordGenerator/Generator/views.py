

from tkinter import *
from tkinter import ttk

class Display():

    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry('300x300')
        master.resizable(False, False)
         # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        self.label = Label(master, text = "Password: ")

        self.label.pack()

        self.new_PassButton = Button(master, text = "Generate Password", command=self.new_button)
        self.new_PassButton.pack()

        #self.old_PassButton = Button(master, text="Saved Passwords", command=self.saved_button)
        #self.old_PassButton.pack()

        #self.close_button = Button(master, text="Quit", command=master.quit)
        #self.close_button.pack()

    def new_button(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')

    def saved_button(self):
        showinfo(title='Information',
                 message='Hello, Tkinter!')


if __name__ == "__main__":
    root = Tk() # first thing needed for tkinter
    my_gui = Display(root)
    root.mainloop()
