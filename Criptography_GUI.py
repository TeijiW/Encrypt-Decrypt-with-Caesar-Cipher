from tkinter import *
import tkinter.ttk as ttk

master = Tk()
master.resizable(width=False, height=False)
w = 400
h = 300
sw = master.winfo_screenwidth()
sh = master.winfo_screenheight()
sw = int((sw/2) - (w/2))
sh = int((sh/2) - (h/2))
flat = ttk.Style()
back = "#98979b"
master.geometry("{}x{}+{}+{}".format(w,h,sw,sh))
menu = Frame(master)
encryptmenu = Frame(master)
decryptmenu = Frame(master)
imageencrypt = PhotoImage(file="C:\Python Projects\Criptography GUI\EncryptButton.png", master=master)
imagedecrypt = PhotoImage(file="C:\Python Projects\Criptography GUI\DecryptButton.png", master=master)
master.configure(background=back)


def start(): 
    encryptmenu.destroy()
    decryptmenu.destroy()
    
    menu.pack()
    
    
    encryptbutton = Button(menu, text="Encrypt", image=imageencrypt, borderwidth=0, highlightthickness=0)
    encryptbutton.pack(anchor=CENTER)
    
    decryptbutton = Button(menu, text="Decrypt", image=imagedecrypt, borderwidth=0, highlightthickness=0)
    decryptbutton.pack(anchor=CENTER)

start()     


master.mainloop()
