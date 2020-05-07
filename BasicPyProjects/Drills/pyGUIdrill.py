from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
import os
import time
import shutil

import pyGUIdrill_func

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.master.minsize(600,175)
        self.master.maxsize(600,175)
        self.master.title("Check files")
        
        load_gui(self)
        
def load_gui(self):
    self.btn_browse = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: pyGUIdrill_func.askdirectory(self,0))
    self.btn_browse.grid(row=1,column=0,padx=(20,0),pady=(20,0))
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: pyGUIdrill_func.askdirectory(self,1))
    self.btn_browse2.grid(row=2,column=0,padx=(20,0),pady=(20,0))
    self.btn_chkfiles = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: pyGUIdrill_func.getfiles(self))
    self.btn_chkfiles.grid(row=3,column=0,rowspan=2,padx=(20,0),pady=(20,0))
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: pyGUIdrill_func.ask_quit(self))
    self.btn_close.grid(row=3,column=1,rowspan=2,padx=(20,0),pady=(20,0),sticky=E)

    self.txt_filepath = tk.Entry(self.master,width=72,text='')
    self.txt_filepath.insert(END,'Source Directory')
    self.txt_filepath.grid(row=1,column=1,padx=(20,0),pady=(20,0),sticky=NSEW)
    self.txt_filepath2 = tk.Entry(self.master,width=72,text='')
    self.txt_filepath2.insert(END,'Destination Directory')
    self.txt_filepath2.grid(row=2,column=1,padx=(20,0),pady=(20,0),sticky=NSEW)

    pyGUIdrill_func.create_db(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    
    
    root.mainloop()
