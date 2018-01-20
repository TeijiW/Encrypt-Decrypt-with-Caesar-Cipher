from tkinter import *
from tkinter import font
import tkinter.ttk as ttk



master = Tk()
master.resizable(width=False, height=False)
w = 600
h = 400
sw = master.winfo_screenwidth()
sh = master.winfo_screenheight()
sw = int((sw/2) - (w/2))
sh = int((sh/2) - (h/2))
back = "#98979b"
master.geometry("{}x{}+{}+{}".format(w,h,sw,sh))
menu = Frame(master)
encryptmenu = Frame(master)
decryptmenu = Frame(master)
mainfont = font.Font(family="Cabin",size="25") 
secundaryfont = font.Font(family="Cabin",size="15")
entryfont = font.Font(family="Cabin", size="12")
master.configure(background=back)
menu.configure(bg=back)
encryptmenu.configure(bg=back)
decryptmenu.configure(bg=back)

def restart():
    encryptmenu.grid_forget()
    decryptmenu.grid_forget()
    
    menu.pack()

def start(): 
    encryptmenu.grid_forget()
    decryptmenu.grid_forget()
    
    menu.pack()
    
    encryptbutton = Button(menu, text="Encrypt", relief="flat", bg=back, activebackground=back, font=mainfont, command=encrypt)
    encryptbutton.pack(side=TOP)
    
    decryptbutton = Button(menu, text="Decrypt", relief="flat", bg=back, activebackground=back, font=mainfont, command=decrypt)
    decryptbutton.pack(side=TOP)
    
def encrypt():
    decryptmenu.grid_forget()
    menu.pack_forget()

    encryptmenu.grid()
    
    labelmessage = Label(encryptmenu, text="Message:", relief="flat", bg=back, activebackground=back, font=secundaryfont)
    labelmessage.grid(row=0, column=1)
    
    scrollbar2 = Scrollbar(encryptmenu)
    scrollbar2.grid(row=0, column=3, sticky=S+N)
    entrymessage = Text(encryptmenu, relief="flat", font=entryfont, height=5, width=37, yscrollcommand=scrollbar2.set, wrap=WORD)
    entrymessage.grid(row=0, column=2, sticky=W)
    scrollbar2.config(command=entrymessage.yview)
    
    okbutton = Button(encryptmenu, relief="ridge", font=secundaryfont, text="Encrypt!", bg=back, activebackground=back)
    okbutton.grid(row=1,column=1, sticky=S)
    
    backbutton = Button(encryptmenu, relief="ridge", font=secundaryfont, text="<<< Back", bg=back, activebackground=back, command=restart)
    backbutton.grid(row=3, column=1, sticky=N)
    
    labelmessage4 = Label(encryptmenu, relief="flat", font=secundaryfont, text="Rotations: ", bg=back, activebackground=back)
    labelmessage4.grid(row=2, column=2, sticky=W)
    
    rotationoption = Spinbox(encryptmenu, relief="flat", font=entryfont, from_=1, to=26, increment=1, width=2)
    rotationoption.grid(row=2, column=2, sticky=N)
     
    labelmessage2 = Label(encryptmenu, text="Encrypted Message:", relief="flat", bg=back, activebackground=back, font=secundaryfont)
    labelmessage2.grid(row=4, column=1)
    
    scrollbar1 = Scrollbar(encryptmenu)
    scrollbar1.grid(row=4, column=3, sticky=S+N)
    encryptedmessage = Text(encryptmenu, relief="flat", font=entryfont, height=5, width=37, yscrollcommand=scrollbar1.set, wrap=WORD)
    encryptedmessage.grid(row=4, column=2, sticky=W)
    scrollbar1.config(command=encryptedmessage.yview)
    
def decrypt():
    encryptmenu.grid_forget()
    menu.pack_forget() 
    
    decryptmenu.grid()
    
    labelmessage3 = Label(decryptmenu, text="Encrypted Message: ", relief="flat", bg=back, activebackground=back, font=secundaryfont)
    labelmessage3.grid(row=0, column=1) 
    
    entryencryptedmessage = Text(decryptmenu, relief="flat", font=entryfont, height=5, width=37)
    entryencryptedmessage.grid(row=0, column=2, sticky=W)
    
    okbutton = Button(decryptmenu, relief="ridge", font=secundaryfont, text="Decrypt!", bg=back, activebackground=back)
    okbutton.grid(row=1,column=1)
    
    backbutton = Button(decryptmenu, relief="ridge", font=secundaryfont, text="<<< Back", bg=back, activebackground=back, command=restart)
    backbutton.grid(row=2, column=1)
    
    
start()     


master.mainloop()
