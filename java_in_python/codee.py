import os
import time
print("Welcome to python environment")
name=input("Enter name of java file to be compiled:\t")
x=os.path.exists(name)
y=name.endswith('.java')
name=name[:-5]
if x==True and y==True:
    print("Compiling your code")
    for i in range(10):
        print(".")
        time.sleep(1)
    os.system("javac"+" "+name+".java")
    print("\nRunning java code")
    for i in range(10):
        print(".")
        time.sleep(1)
    os.system("java"+" "+name)
else:
    print("\nSorry,file not found!")
time.sleep(2)
print("\nWelcome back to python environment")
