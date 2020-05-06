from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.master.minsize(600,175)
        self.master.maxsize(600,175)
        self.master.title("Check files")
        
        load_gui(self)
        
def load_gui(self):
    self.btn_browse = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse.grid(row=1,column=0,padx=(20,0),pady=(20,0))
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=2,column=0,padx=(20,0),pady=(20,0))
    self.btn_chkfiles = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_chkfiles.grid(row=3,column=0,rowspan=2,padx=(20,0),pady=(20,0))
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=3,column=1,rowspan=2,padx=(20,0),pady=(20,0),sticky=E)

    self.txt_filepath = tk.Entry(self.master,width=72,text='')
    self.txt_filepath.grid(row=1,column=1,padx=(20,0),pady=(20,0),sticky=NSEW)
    self.txt_filepath2 = tk.Entry(self.master,width=72,text='')
    self.txt_filepath2.grid(row=2,column=1,padx=(20,0),pady=(20,0),sticky=NSEW)


    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
