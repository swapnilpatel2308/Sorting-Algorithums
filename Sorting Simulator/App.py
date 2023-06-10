from tkinter import *
import tkinter as tk
import subprocess

root = tk.Tk()

root.geometry("250x180")
root.resizable(False,False)
root.configure(background="#00ffff")

def run_is_fa():
    subprocess.call(['python', 'is_fa.py'])

bubble = Button(root,text="Bubble Sort",command=lambda: subprocess.call(['python', 'bubble.py'])).place(x=10,y=10)
bucket = Button(root,text="Bucket Sort",command=lambda: subprocess.call(['python', 'bucket.py'])).place(x=90,y=10)
heap = Button(root,text="Heap Sort",command=lambda: subprocess.call(['python', 'heap.py'])).place(x=170,y=10)
insertion = Button(root,text="Insertion Sort",command=lambda: subprocess.call(['python', 'insertion.py'])).place(x=10,y=50)
merge = Button(root,text="Merge Sort",command=lambda: subprocess.call(['python', 'merge.py'])).place(x=95,y=50)
quick = Button(root,text="Quick Sort",command=lambda: subprocess.call(['python', 'quick.py'])).place(x=170,y=50)
redix = Button(root,text="Redix Sort",command=lambda: subprocess.call(['python', 'redix.py'])).place(x=10,y=90)
selection = Button(root,text="Selection Sort",command=lambda: subprocess.call(['python', 'selection.py'])).place(x=80,y=90)
shell = Button(root,text="Shell Sort",command=lambda: subprocess.call(['python', 'shell.py'])).place(x=170,y=90)
tim = Button(root,text="Tim Sort",command=lambda: subprocess.call(['python', 'tim.py'])).place(x=90,y=130)

root.mainloop()