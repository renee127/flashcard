# a flashcard app using
# tkinter

import tkinter as tk

class Flashcard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.greet = tk.Button(self)
        self.greet['text'] = 'the word\n(click for the meaning)'
        self.greet['command'] = self.say_hi
        self.greet.pack(side = 'top')

        self.quit = tk.Button(self, text='Quit', fg='red',
                              command=self.master.destroy)
        self.quit.pack(side='bottom')

    def say_hi(self):
        print('hi there')

root = tk.Tk()
app = Flashcard(master=root)
app.mainloop()

print('done')