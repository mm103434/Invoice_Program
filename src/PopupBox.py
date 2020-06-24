import tkinter as tk

class PopupBox:
    def __init__(self):
        self.btn_txt = ""
        self.root= tk.Tk()

        self.label1 = tk.Label(self.root, text='Enter the Category:'
                                               '(CS, DG, M, PR, etc.')
        self.canvas1 = tk.Canvas(self.root, width = 400, height = 300)
        self.canvas1.pack()

        self.entry1 = tk.Entry (self.root)
        self.canvas1.create_window(200, 140, window=self.entry1)

    def check_cat(self):
        x1 = self.entry1.get()
        self.btn_txt = x1
        #print(self.btn_txt)
        self.root.destroy()



    def makeWindow(self, decr):

        label1 = tk.Label(text="Enter a category for:\n" + decr + ":\n(CS, DG, M, PR, Etc..")
        cat = button1 = tk.Button(text='Enter Category:', command=self.check_cat)
        self.root.title("Invoice Prog")
        self.canvas1.create_window(200, 180, window=button1)
        self.canvas1.create_window(200, 100, window=label1)

        self.root.mainloop()
        return self.btn_txt
