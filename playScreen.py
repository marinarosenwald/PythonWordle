import tkinter as tk
from tkinter import ttk
  

#initialize screen 
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="WORDLE").grid(column=0, row=0)

#create a button for each letter - same order of a keyboard 
keybaord = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
row = 2
for line in keybaord:
    col = 0
    for letter in line: 
        ttk.Button(frm, text=letter, command=root.destroy).grid(column=col, row=row)
        col += 1
    row += 1

#create quit button 
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=11, row=0)
root.mainloop()