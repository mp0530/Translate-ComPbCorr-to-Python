# Things to be done in near future: 
# 1. GUI Design
# 2. Clean code with Class or Function
# 3. Started other UserForm

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
UserForm1 = tk.Tk() #create the windows
UserForm1.config(bg = "yellow")
font1 = Font(size = 12, slant = "italic", weight = "bold")
font2 = Font(size = 9, weight = "bold")
font3 = Font(size = 9, weight = "bold",slant = "italic")
font4 = Font(size = 7)
# Title
UserForm1.title("UserForm1")
# Size
UserForm1.geometry("600x800")
UserForm1.minsize(width=200,height=200)

label1 = tk.Label(UserForm1,text = "Composition of common-lead:", font = font3, fg = "#008000", bg = "yellow")
label2 = tk.Label(UserForm1,text = "Stacey - Kramers at",font = font2,fg = "green",bg = "yellow")
label3 = tk.Label(UserForm1,text = "Ga",font = font2,fg = "green",bg = "yellow")
label4 = tk.Label(UserForm1,text = "OR:",font = font2,fg = "green",bg = "yellow")
label5 = tk.Label(UserForm1,text = "206/204",font = font2,fg = "green",bg = "yellow")
label6 = tk.Label(UserForm1,text = "207/204",font = font2,fg = "green",bg = "yellow")
label7 = tk.Label(UserForm1,text = "208/204",font = font2,fg = "green",bg = "yellow")
label8 = tk.Label(UserForm1,text = "Age of lead-loss",font = font2,fg = "green",bg = "yellow")
label9 = tk.Label(UserForm1,text = "Ga",font = font2,fg = "green",bg = "yellow")
label10 = tk.Label(UserForm1,text = "Correlation of errors in 206Pb/238U and 207Pb/235U",font = font3,fg = "green",bg = "yellow")
label11 = tk.Label(UserForm1,text = "Using apparent error correlations from GLITTER output!",font = font4 ,fg = "green",bg = "yellow")

text1 = tk.Text(UserForm1,width = 6,height = 1.4)
text2 = tk.Text(UserForm1,width = 6,height = 1.4)
text3 = tk.Text(UserForm1,width = 6,height = 1.4)
text4 = tk.Text(UserForm1,width = 6,height = 1.4)
text5 = tk.Text(UserForm1,width = 6,height = 1.4)

separator1 = ttk.Separator(UserForm1,orient = "horizontal")

ok = tk.Button(UserForm1,text = "OK",font = font1,bg = "green",fg = "yellow",width = 8,height = 1)
cancel = tk.Button(UserForm1,text = "Cancel",font = font1,bg = "green",fg = "yellow",width=8,height=1,command = UserForm1.quit)
checkbox1 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Specify lead composition:",font = font2,fg = "green")
checkbox2 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Constant error correlation\ncoefficient of:",justify = "left",font = font2,fg = "green")
checkbox3 = tk.Checkbutton(UserForm1,bg = "yellow",activebackground = "yellow",text = "Use observed error correlations\nfrom worksheet, but use a constant\nvalue for blanks:",justify = "left",font = font2,fg = "green")


label1.place(relx = 0.06, rely = 0.2)
label2.place(relx = 0.06, rely = 0.25)
label3.place(relx = 0.55, rely = 0.25)
label4.place(relx = 0.1, rely = 0.3)
label5.place(relx = 0.15, rely = 0.4)
label6.place(relx = 0.35, rely = 0.4)
label7.place(relx = 0.55, rely = 0.4)
label8.place(relx = 0.1, rely = 0.5)
label9.place(relx = 0.55, rely = 0.5)
label10.place(relx = 0.1, rely = 0.55)
label11.place(relx = 0.1, rely = 0.68)

text1.place(relx = 0.4, rely = 0.25)
text2.place(relx = 0.15, rely = 0.45)
text3.place(relx = 0.35, rely = 0.45)
text4.place(relx = 0.55, rely = 0.45)
text5.place(relx = 0.4, rely = 0.5)

ok.place(relx = 0.6, rely = 0.06)
cancel.place(relx = 0.6, rely = 0.14)

checkbox1.place(relx = 0.06, rely = 0.35)
checkbox2.place(relx = 0.06, rely = 0.62)
checkbox3.place(relx = 0.06, rely = 0.7)

separator1.place(rely = 0.8)


UserForm1.mainloop() #常駐主視窗
