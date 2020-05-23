import tkinter as tk
from tkinter.font import Font
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys
if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
# -----------------------------------------------------------

UserForm1 = tk.Tk() #create the windows
font1 = Font(size = 14, slant = "italic", weight = "bold")
# Title
UserForm1.title("UserForm1")
# Size
UserForm1.geometry("400x400")
UserForm1.minsize(width=200,height=200)
# UserForm1.resizable(False,False)
ok = tk.Button(text = "OK",font = font1,bg = "green",fg = "yellow")
cancel = tk.Button(text = "Cancel",font = font1,bg = "green",fg = "yellow")
# ok.config(bg="skyblue")
ok.pack()
cancel.pack()
UserForm1.mainloop() #常駐主視窗
