from UserForm1 import UserForm1
from UserForm3 import UserForm3

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
from tkinter import ttk
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys
if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

class Main:
    def __init__(self,sheet):
        self.execute(sheet)
    def execute(self,sheet):
        if sheet == "data":
            root = tk.Tk()
            app = UserForm1(root)
            root.mainloop()

        elif sheet == "input":
            root = tk.Tk()
            app = UserForm3(root)
            root.mainloop()
x = Main("input")