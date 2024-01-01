from cryptography.fernet import Fernet

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file= open("key.key","rb")
    key=file.read()
    file.close()
    return key


key=load_key()
fer=Fernet(key)

#write_key()

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data=line.rstrip()
            user, passw = data.split("|")
            print("UserName: ",user, " | Password: ", fer.decrypt(passw.encode()).decode(), "\n")

def add():
    name= input ("Enter Account Name: ")
    pwd= input ("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode= input("Add a new password or View existing passwords? \n ADD or VIEW[Press Q to QUIT]:  ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()
    else:
        print("Invalid Response")
        continue