from tkinter import *
import tkinter as tk
from tkinter import filedialog

import pyGUIdrill

def askdirectory(self,which_button):
    dirname = filedialog.askdirectory()
    if which_button == 0:
        self.txt_filepath.delete(0,END)
        self.txt_filepath.insert(0,dirname)
    if which_button == 1:
        self.txt_filepath2.delete(0,END)
        self.txt_filepath2.insert(0,dirname)
        
    ## print(dirname)

if __name__ == "__main__":
    pass
