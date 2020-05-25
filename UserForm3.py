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

ga = 100
UserForm3 = tk.Tk() #create the windows
UserForm3.config(bg = "yellow")
UserForm3.geometry("500x800")

font1 = Font(size = 9, weight = "bold")
font2 = Font(size = 9, weight = "bold",slant = "italic")
font3 = Font(size = 9)
font4 = Font(size = 16, weight = "bold")
font5 = Font(size = 11, weight = "bold")

ok = tk.Button(UserForm3,text = "OK",font = font5,bg = "green",fg = "yellow",width = 8,height = 1)
cancel = tk.Button(UserForm3,text = "Cancel",font = font5,bg = "green",fg = "yellow",width=8,height=1,command = UserForm3.quit)

label1 = tk.Label(UserForm3,text = "Instrumental discrimination of U and Th",font = font1,fg = "green",bg = "yellow")
label2 = tk.Label(UserForm3,text = "Factor",font = font1,fg = "green",bg = "yellow")
label3 = tk.Label(UserForm3,text = "±",font = font1,fg = "green",bg = "yellow")
label4 = tk.Label(UserForm3,text = "(1 σ)",font = font1,fg = "green",bg = "yellow")
label5 = tk.Label(UserForm3,text = "Plague vs. Cholera - please make your choice !",font = font2,fg = "green",bg = "yellow")
label6 = tk.Label(UserForm3,text = "U-Pb errors are highly correlated, but GLITTER in\n\
principle treats them as uncorrelated. This causes\n\
problems for calculation of corrected 207Pb/206Pb\n\
ratios and ages, and becomes very prominet when\n\
trying to plot TW concordias from TW style output.\n\
These routines do not solve the problem, but have\n\
been designed to create consistent output.",font = font3,fg = "green",bg = "yellow",justify = "left")
label7 = tk.Label(UserForm3,text = "\n\
GLITTER commonly reports apparent (spurious) error.\n\
Choosing this option will allow you to specify a constant\n\
error correlation coefficient. Error propogation of\n\
corrected data will be done accordingly, and errors on\n\
corrected ratios are internally consistent. But the error on\n\
corrected 207Pb/206Pb ratios will appear smaller than on\n\
the raw ratios!",font = font3,fg = "green",bg = "yellow",justify = "left")

checkbox1 = tk.Checkbutton(UserForm3,text = "No correction",bg = "yellow",activebackground = "yellow",font = font1,fg = "green")
checkbox2 = tk.Checkbutton(UserForm3,text = "Use empirical correction factor",bg = "yellow",activebackground = "yellow",font = font1,fg = "green")
checkbox3 = tk.Checkbutton(UserForm3,text = "Use apparent error correlations from GLITTER",bg = "yellow",activebackground = "yellow",font = font3,fg = "green")
checkbox4 = tk.Checkbutton(UserForm3,text = "Ignore apparent error correlations from GLITTER",bg = "yellow",activebackground = "yellow",font = font3,fg = "green",justify = "left")

text1 = tk.Text(UserForm3,width = 4,height = 1,font=("Helvetica", 18))
text2 = tk.Text(UserForm3,width = 4,height = 1,font=("Helvetica", 18))

separator1 = ttk.Separator(UserForm3,orient = "horizontal")
separator2 = ttk.Separator(UserForm3,orient = "horizontal")

label1.place(relx = 0.05, rely = 0.02, anchor = "nw")
checkbox1.place(relx = 0.2, rely = 0.08, anchor = "nw")
checkbox2.place(relx = 0.2, rely = 0.13, anchor = "nw")
label2.place(relx = 0.1, rely = 0.22, anchor = "w")
text1.place(relx = 0.35, rely = 0.22, anchor = "center")
label3.place(relx = 0.5, rely = 0.22, anchor = "center")
text2.place(relx = 0.65, rely = 0.22, anchor = "center")
label4.place(relx = 0.8, rely = 0.22, anchor = "w")
separator1.place(rely = 0.3, relwidth = 2, anchor = "center")
separator1.lower()
label5.place(relx = 0.5, rely = 0.3, anchor = "center")
label6.place(relx = 0.5, rely = 0.335, anchor = "n")
checkbox3.place(relx = 0.1, rely = 0.54, anchor = "nw")
checkbox4.place(relx = 0.1, rely = 0.59, anchor = "nw")
separator2.place(rely = 0.65, relwidth = 2)
label7.place(relx = 0.5, rely = 0.65, anchor = "n")
ok.place(relx = 0.35, rely = 0.93, anchor = "center")
cancel.place(relx = 0.65, rely = 0.93, anchor = "center")
UserForm3.mainloop()
