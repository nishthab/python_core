import os

# File Name
dir_name = os.getcwd()
print("Current working directory-->", dir_name)

fname = dir_name + "\\Files\\sample.txt"
print("File Name--->", fname)

print("-------------------------------------")

# create the empty file
#fhandle = open(fname,"w")
fhandle = open(fname , "a")
fhandle.write("This is my first file 1.....\n")
fhandle.write("This is my first file 2.....\n")
fhandle.write("This is my first file 3.....\n")

#append the contents to the file

fhandle.close()
print("File created succesfully")
print("-------------------------------------")

#Read the file
fread = open(fname,"r")# open(fname,"r") both are same bydefault mode is r

# read, readling, readlines

print("read method")

contents = fread.read(10)
print("contents-->", contents)


contents = fread.read(10)
print("contents-->", contents)

contents = fread.read()
print("contents-->", contents)

# Move the cursor to the begining of the file
fread.seek(0)
print("--------------------------------------")
print("readlint method")

contents = fread.readline()
while(contents):
    print(contents)
    contents = fread.readline()

print("------------------------------------")
# Move the cursor to the begining of the file
fread.seek(0)

print("------------------------------------")
print("readlines method")

all_lines = fread.readlines();
print(type(all_lines))
print(all_lines)


fread.close()
