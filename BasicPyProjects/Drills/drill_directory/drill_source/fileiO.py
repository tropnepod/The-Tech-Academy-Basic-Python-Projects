import os   # importing the os methods
import time # importing time methods

directory = os.getcwd()     # set the current working directory in a variable
files = []  # creating an array for the file names
dMod = []   # creating an array for the modification dates


for filename in os.listdir(directory):  # loop through directory
    if filename.endswith('.txt'):   # condition to find the desired files
        files.append(filename)      # adding filename to files array
        modtime = os.path.getmtime((directory + '\\' + filename)) # getting modification time
        local_time = time.ctime(modtime)    # converting modtime to more user friendly time
        dMod.append(local_time) # adding modification time to dMod array
    else:
        continue

for (f,d) in zip(files, dMod): #loop through arrays to print information
    print("File Name: {}\nDate Modified: {}\n".format(f,d))
