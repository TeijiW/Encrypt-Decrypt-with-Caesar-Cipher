from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import string

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
abclist = string.ascii_lowercase + string.ascii_lowercase

def encryptsystem(): 
    encryptedmessage.delete("1.0", END)
    crypted = []
    str1 = entrymessage.get("1.0", END+"-1c")
    str1 = str1.lower() 
    strlist = list(str1)
    rot = int(rotwidget.get())
    for x in strlist:
        if x not in abclist:
            crypted.append("#")
        else:
            n = abclist.find(x)
            crypted.append(abclist[n+rot])
    
    str1 = "".join(crypted)
    encryptedmessage.insert("1.0", str1)
    
def decryptsystem():
    decryptedmessage.delete("1.0", END)
    decrypted = []
    str1 = entryencryptedmessage.get("1.0", END+"-1c")
    strl = str1.lower()
    strlist = list(str1)
    cont = -1 
    rot = -1
    mastercont = 0
    while True:
        cont += 1
        if cont == len(strlist):
            cont = 0
            rot -= 1
            mastercont += 1
            decrypted = "".join(decrypted)
            decryptedmessage.insert("1.0", "Rotation {}: {} \n".format(mastercont, decrypted))
            decrypted = []
            if mastercont == 25:
                break
        m = strlist[cont]
        n = abclist.find(m)
        n = n+26
        if m == "#" or m == " ":
            decrypted.append(" ")
        else:
            decrypted.append(abclist[n+rot])
    
    
    
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
    global entrymessage, rotwidget, encryptedmessage
    
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
    
    okbutton = Button(encryptmenu, relief="ridge", font=secundaryfont, text="Encrypt!", bg=back, activebackground=back, command=encryptsystem, width=8)
    okbutton.grid(row=1,column=1, sticky=S)
    
    backbutton = Button(encryptmenu, relief="ridge", font=secundaryfont, text="<<< Back", bg=back, activebackground=back, command=restart, width=8)
    backbutton.grid(row=3, column=1, sticky=N)
    
    labelmessage4 = Label(encryptmenu, relief="flat", font=secundaryfont, text="Rotations: ", bg=back, activebackground=back)
    labelmessage4.grid(row=2, column=2, sticky=W)
    
    rotwidget = Spinbox(encryptmenu, relief="flat", font=entryfont, from_=1, to=26, increment=1, width=2)
    rotwidget.grid(row=2, column=2, sticky=N)
     
    labelmessage2 = Label(encryptmenu, text="Encrypted Message:", relief="flat", bg=back, activebackground=back, font=secundaryfont)
    labelmessage2.grid(row=4, column=1)
    
    scrollbar1 = Scrollbar(encryptmenu)
    scrollbar1.grid(row=4, column=3, sticky=S+N)
    encryptedmessage = Text(encryptmenu, relief="flat", font=entryfont, height=5, width=37, yscrollcommand=scrollbar1.set, wrap=WORD)
    encryptedmessage.grid(row=4, column=2, sticky=W)
    scrollbar1.config(command=encryptedmessage.yview)
    
def decrypt():
    global decryptedmessage, entryencryptedmessage
    
    encryptmenu.grid_forget()
    menu.pack_forget() 
    
    decryptmenu.grid()
    
    labelmessage3 = Label(decryptmenu, text="Encrypted Message:", relief="flat", bg=back, activebackground=back, font=secundaryfont)
    labelmessage3.grid(row=0, column=1, sticky=W) 
    
    scrollbar3 = Scrollbar(decryptmenu)
    scrollbar3.grid(row=0, column=3, sticky=S+N)
    entryencryptedmessage = Text(decryptmenu, relief="flat", font=entryfont, height=5, width=36, yscrollcommand=scrollbar3.set, wrap=WORD)
    entryencryptedmessage.grid(row=0, column=2, sticky=W)
    scrollbar3.config(command=entryencryptedmessage.yview)
    
    okbutton = Button(decryptmenu, relief="ridge", font=secundaryfont, text="Decrypt!", bg=back, activebackground=back, width=8, command=decryptsystem)
    okbutton.grid(row=1,column=1, sticky=N)
    
    backbutton = Button(decryptmenu, relief="ridge", font=secundaryfont, text="<<< Back", bg=back, activebackground=back, command=restart, width=8)
    backbutton.grid(row=2, column=1, sticky=S)
    
    labelmessage5 = Label(decryptmenu, text="Decrypted Message: ", relief="flat", bg=back, activebackground=back, font=secundaryfont)
    labelmessage5.grid(row=3, column=1)
    
    scrollbar4 = Scrollbar(decryptmenu)
    scrollbar4.grid(row=3, column=3, sticky=S+N)
    decryptedmessage = Text(decryptmenu, relief="flat", font=entryfont, height=5, width=36, yscrollcommand=scrollbar4.set, wrap=WORD)
    decryptedmessage.grid(row=3, column=2, sticky=W)
    scrollbar4.config(command=decryptedmessage.yview)
    
    
start()     


master.mainloop()
