import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=3)

buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0", ".", "=",
]

row = 1
col = 0
for button in buttons:
    action = lambda x=button: entry.insert(tk.END, x)
    tk.Button(root, text=button, width=5, command=action).grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

root.mainloop()
