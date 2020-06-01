import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from UserForm1 import UserForm1
# ---------- To solve resolution issue in Windows -----------
import ctypes
import sys

if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
# -----------------------------------------------------------
class UserForm3:
    def __init__(self,master):
        self.UserForm3 = master #create the windows
        self.UserForm3.config(bg = "yellow")
        self.UserForm3.geometry("500x800")
        self.str = "\
        Choosing this option will allow you to specify a constant\n\
        error correlation coefficient. Error propagation of\n\
        corrected data will be done accordingly, and errors on\n\
        corrected 207Pb/206Pb ratios will appear smaller than on\n\
        the raw ratios!"
        self.str0 = "\
        GLITTER commonly reports apparent (spurious) error.\n\
        Choosing this option will allow you to specify a constant\n\
        error correlation coefficient. Error propogation of\n\
        corrected data will be done accordingly, and errors on\n\
        corrected ratios are internally consistent. But the error on\n\
        corrected 207Pb/206Pb ratios will appear smaller than on\n\
        the raw ratios!"
        self.str1 = "\
        Choosing this option will allow you to specify a constant\n\
        error correlation coefficient. Error propagation of\n\
        corrected data will be done accordingly, and errors on\n\
        corrected 207Pb/206Pb ratios will appear smaller than on\n\
        the raw ratios!"

        self.font1 = Font(size = 9, weight = "bold")
        self.font2 = Font(size = 9, weight = "bold",slant = "italic")
        self.font3 = Font(size = 9)
        self.font4 = Font(size = 11, weight = "bold")

        self.ok = tk.Button(self.UserForm3,text = "OK",font = self.font4,bg = "green",fg = "yellow",width = 8,height = 1,command = self.ok)
        self.cancel = tk.Button(self.UserForm3,text = "Cancel",font = self.font4,bg = "green",fg = "yellow",width=8,height=1,command = self.UserForm3.quit)

        self.label1 = tk.Label(self.UserForm3,text = "Instrumental discrimination of U and Th",font = self.font1,fg = "green",bg = "yellow")
        self.label2 = tk.Label(self.UserForm3,text = "Factor",font = self.font1,fg = "green",bg = "yellow")
        self.label3 = tk.Label(self.UserForm3,text = "±",font = self.font1,fg = "green",bg = "yellow")
        self.label4 = tk.Label(self.UserForm3,text = "(1 σ)",font = self.font1,fg = "green",bg = "yellow")
        self.label5 = tk.Label(self.UserForm3,text = "Plague vs. Cholera - please make your choice !",font = self.font2,fg = "green",bg = "yellow")
        self.label6 = tk.Label(self.UserForm3,text = "U-Pb errors are highly correlated, but GLITTER in\n\
        principle treats them as uncorrelated. This causes\n\
        problems for calculation of corrected 207Pb/206Pb\n\
        ratios and ages, and becomes very prominet when\n\
        trying to plot TW concordias from TW style output.\n\
        These routines do not solve the problem, but have\n\
        been designed to create consistent output.",font = self.font3,fg = "green",bg = "yellow",justify = "left")
        self.label7 = tk.Label(self.UserForm3,text= self.str
                               ,font = self.font3,fg = "green",bg = "yellow",justify = "left")
        self.var_chk1 = tk.IntVar()
        self.var_chk2 = tk.IntVar()

        self.checkbox1 = tk.Radiobutton(self.UserForm3,text = "No correction",bg = "yellow",
                                        activebackground = "yellow",font = self.font1,fg = "green",
                                        variable = self.var_chk1, value = 0, command = self.deselect)
        self.checkbox2 = tk.Radiobutton(self.UserForm3,text = "Use empirical correction factor",bg = "yellow",
                                        activebackground = "yellow",font = self.font1,fg = "green",
                                        variable = self.var_chk1, value = 1, command = self.deselect)
        self.checkbox3 = tk.Radiobutton(self.UserForm3,text = "Use apparent error correlations from GLITTER",
                                        bg = "yellow",activebackground = "yellow",font = self.font3,fg = "green",
                                        variable = self.var_chk2, value = 1, command = self.strchange)
        self.checkbox4 = tk.Radiobutton(self.UserForm3,text = "Ignore apparent error correlations from GLITTER",
                                        bg = "yellow",activebackground = "yellow",font = self.font3,fg = "green",
                                        justify = "left",
                                        variable = self.var_chk2, value = 0, command = self.strchange)
        self.factor = tk.IntVar()
        self.factor.set(1)
        self.text1 = tk.Entry(self.UserForm3, width = 5, font=("Helvetica", 18), state = "disabled",text = self.factor, justify = "center")
        self.text2 = tk.Entry(self.UserForm3, width = 5, font=("Helvetica", 18), state = "disabled", justify = "center")

        self.separator1 = ttk.Separator(self.UserForm3,orient = "horizontal")
        self.separator2 = ttk.Separator(self.UserForm3,orient = "horizontal")

        self.label1.place(relx = 0.05, rely = 0.02, anchor = "nw")
        self.checkbox1.place(relx = 0.2, rely = 0.08, anchor = "nw")
        self.checkbox2.place(relx = 0.2, rely = 0.13, anchor = "nw")
        self.label2.place(relx = 0.1, rely = 0.22, anchor = "w")
        self.text1.place(relx = 0.35, rely = 0.22, anchor = "center")
        self.label3.place(relx = 0.5, rely = 0.22, anchor = "center")
        self.text2.place(relx = 0.65, rely = 0.22, anchor = "center")
        self.label4.place(relx = 0.8, rely = 0.22, anchor = "w")
        self.separator1.place(rely = 0.3, relwidth = 2, anchor = "center")
        self.separator1.lower()
        self.label5.place(relx = 0.5, rely = 0.3, anchor = "center")
        self.label6.place(relx = 0.5, rely = 0.335, anchor = "n")
        self.checkbox3.place(relx = 0.1, rely = 0.54, anchor = "nw")
        self.checkbox4.place(relx = 0.1, rely = 0.59, anchor = "nw")
        self.separator2.place(rely = 0.65, relwidth = 2)
        self.label7.place(relx = 0.5, rely = 0.65, anchor = "n")
        self.ok.place(relx = 0.35, rely = 0.93, anchor = "center")
        self.cancel.place(relx = 0.65, rely = 0.93, anchor = "center")

    def ok(self):
        self.UserForm3.destroy()
        root = tk.Tk()
        app = UserForm1(root)

    def deselect(self):
        if self.var_chk1.get() == 0:
            self.text2.delete(0,"end")
            self.factor.set(1)
            self.text1.config(fg = "gray", state = "disabled")
            self.text2.config(text = "", fg = "gray", state = "disabled")
        else:
            self.factor.set(0.85)
            self.text1.config(fg = "black", state = "normal")
            self.text2.config(fg = "black", state = "normal")
            self.text2.insert(0,0.05)

    def strchange(self):
        if self.var_chk2.get() == 1:
            self.label7.config(text = self.str0)
        else:
            self.label7.config(text = self.str1)


