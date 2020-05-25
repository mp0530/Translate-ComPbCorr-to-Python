import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys

if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
# -----------------------------------------------------------

UserForm4 = tk.Tk() #create the windows
UserForm4.title("Monte-Carlo error estimate")
UserForm4.config(bg = "yellow")
UserForm4.geometry("480x300")

font1 = Font(size = 12, weight = "bold")

ok = tk.Button(UserForm4,text = "OK",font = font1,bg = "green",fg = "yellow",width = 8,height = 1)

label1 = tk.Label(UserForm4,text = "Set number of trials to",font = font1,fg = "green",bg = "yellow")
label2 = tk.Label(UserForm4,text = "n >(>) 100!",font = font1,fg = "green",bg = "yellow")

text1 = tk.Text(UserForm4,width = 4,height = 1,font=("Helvetica", 18))

label1.place(relx = 0.35, rely = 0.4, anchor = "center")
text1.place(relx = 0.85, rely = 0.4, anchor = "e")
label2.place(relx = 0.3, rely = 0.65, anchor = "center")
ok.place(relx = 0.9, rely = 0.9, anchor = "se")
UserForm4.mainloop()
