import string
import os
def encrypt():
    os.system("cls")
    print("Welcome, this program will encrypt your message.") 
    print("------------------------------------------------") 
    str = input("Message: ")
    str = str.lower()
    abclist = string.ascii_lowercase + string.ascii_lowercase  #Creating lowercase alphabet list (2X to ensure) 
    strlist = list(str) 
    while True: #GEnsuring that the number of rotations is entered correctly
        rot = int(input("Number of rotations: "))
        if rot > 25: 
            os.system("cls")
            print("Invalid Number!") 
            print("") 
        else: 
            break

    cripted = [] 
    for x in strlist:  #Encryption system
        if x not in abclist: 
            cripted.append("#")
        else:
            n = abclist.find(x)
            cripted.append(abclist[n+rot])

    str = "".join(cripted)
    os.system("cls") 
    print("Encrypted message: {}".format(str))

    input("Press any key to exit...")
    
def decrypt():
    os.system("cls")
    print("Welcome, this program will decrypt your message.") 
    print("------------------------------------------------") 
    str = input("Message: ")
    abclist = string.ascii_lowercase + string.ascii_lowercase
    str = str.lower() 
    strlist = list(str)
    cont = -1
    rot = -1
    mastercont = 0
    newlist = []
    os.system("cls")
    while True:
        cont += 1
        if cont == len(strlist):
            cont = 0
            rot -= 1 
            mastercont += 1
            newlist = "".join(newlist)
            print("Rotation {}: {}".format(mastercont,newlist))
            print("----------------------------------------------------------------")
            print("")
            print("")
            newlist = []
            if mastercont == 25:
                break 
        m = strlist[cont]
        n = abclist.find(m)
        n = n+26
        if m == "#" or m ==" ":
            newlist.append(" ")
        else:
            newlist.append(abclist[n + rot])
    print("")
    print("")
    print("Finish!")
    input("Press any key to exit!")

while True:
    try: 
        print("1 - Encrypt")
        print("2 - Decrypt") 
        print("")
        esc = int(input("Your choice: "))
        if esc == 1 or esc == 2:
            break
        else:
            pass
    except ValueError:
        pass
    os.system("cls")
    print("Invalid Option")
    print("--------------")
if esc == 1: 
    encrypt()
if esc == 2:
    decrypt()
