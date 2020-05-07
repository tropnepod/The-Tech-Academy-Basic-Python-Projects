from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import sqlite3
import os
import time
import shutil

import pyGUIdrill

def ask_quit(self):
    if messagebox.askokcancel('Exit Program','Okay to exit application?'):
        self.master.destroy()
        os._exit(0)

def askdirectory(self,which_button):
    dirname = filedialog.askdirectory()
    if which_button == 0:
        self.txt_filepath.delete(0,END)
        self.txt_filepath.insert(0,dirname)
    if which_button == 1:
        self.txt_filepath2.delete(0,END)
        self.txt_filepath2.insert(0,dirname)
        
    ## print(dirname)

def create_db(self):
    conn = sqlite3.connect('db_filesMoved.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_filesMoved( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fileName TEXT, \
                col_fileModTime TEXT \
                );")
        conn.commit()
    conn.close()
    first_run(self)
    
def first_run(self):
    data = ('Initialize_Data','Initialize_Data')
    conn = sqlite3.connect('db_filesMoved.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("INSERT INTO tbl_filesMoved (col_fileName, col_fileModTime) VALUES (?,?)", ('Initialize_Data','Initialize_Data'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ''
    cur.execute("SELECT COUNT(*) FROM tbl_filesMoved")
    count = cur.fetchone()[0]
    return cur,count
    
def getfiles(self):
    src_dir = self.txt_filepath.get()
    des_dir = self.txt_filepath2.get()
    files = []
    abso_path = []
    dMod = []
    if src_dir == 'Source Directory' or des_dir == 'Destination Directory' or src_dir == des_dir or src_dir == '' or des_dir == '':
        messagebox.showerror("Error in directory selection","Please make sure to select a source directory \nand a destination directory, and \nthat they are different")
    else:
        for filename in os.listdir(src_dir):
            if filename.endswith('.txt'):
                files.append(filename)
                cur_path = os.path.join(src_dir, filename)
                abso_path.append(cur_path)
                modtime = os.path.getmtime(cur_path)
                local_time = time.ctime(modtime)
                dMod.append(local_time)
                final_des = shutil.move(cur_path,des_dir)
            else:
                continue

        def addToDB(self):
            for (f,d) in zip(files,dMod):
                var_fileName = f.strip()
                var_ModTime = d.strip()
                if var_fileName != '' and var_ModTime != '':
                    conn = sqlite3.connect('db_filesMoved.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("INSERT INTO tbl_filesMoved (col_fileName,col_fileModTime) VALUES (?,?)",(var_fileName,var_ModTime))
                        onReset(self)
                    conn.commit()
                    conn.close()

        addToDB(self)
        
        mb_display = '\n'.join(files)
        if mb_display != '':
            messagebox.showinfo("Changes","Files moved:\n{}".format(mb_display))
        else:
            messagebox.showinfo("Changes","No changes made, no files met requirements.")

        #print(src_dir)
        #print(des_dir)

        for (f,d) in zip(files, dMod):
            print("File Name: {}\nDate Modified: {}\n".format(f,d))

        #for path in abso_path:
        #    print(path +'\n')
        
def onReset(self):
    self.txt_filepath.delete(0,END)
    self.txt_filepath.insert(END,'Source Directory')
    self.txt_filepath2.delete(0,END)
    self.txt_filepath2.insert(END,'Destination Directory')



if __name__ == "__main__":
    pass
