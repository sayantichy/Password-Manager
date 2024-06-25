from cryptography.fernet import Fernet

def write_key():
  key= Fernet.generate_key()
  with open("key.key","wb") as key_file:
    key_file.write(key)

write_key()
master_pwd= input("What is the master password? ")

def view():
   with open("password_maneger.txt", 'r') as f:
    for line in f:
      data = line.rstrip()
      user, passw = data.split("|")
      print("User:", user,"Password:", passw)
      



def add():
  user_name= input("User name : " )
  pwd =input("Password: ")
  with open("password_maneger.txt", 'a') as f:
    f.write( user_name + " | " + pwd + "\n" )


while True:
  mode= input("Would you like to add a new password or view existing passwords?(add/view) or press q to quit ").lower()
  if mode=="q":
    break
  if mode== "add":
    add()
  elif mode=="view":
    view()
  else:
    print("Invalid Input")
    continue
