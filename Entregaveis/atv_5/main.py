# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 14/10/2022 
# version ='1.0'
# ---------------------------------------------------------------------------

import json
from argon2 import PasswordHasher
  
argon_pwd = PasswordHasher() 
  
def register(email, pwd):
  
  arr = []
  try:
    with open("database.json", "r") as read_it:
      data = json.load(read_it)
        
    if(len(data) >= 1):
      for i in data: 
        arr.append(i)
  except:
    pass

  pwd_hash = argon_pwd.hash(pwd)
  salt = pwd_hash.split("$")
  
  dict_input = {
    "email" : email,
    "password" : pwd_hash,
    "salt": salt[4]
  }
  
  arr.append(dict_input)
  
  out_file = open("database.json", "w")
  
  json.dump(arr, out_file, indent=4)
  
  out_file.close()
  return True

def login():
  arr = []
  try:
    with open("database.json", "r") as read_it:
      data = json.load(read_it)
        
    if(len(data) >= 1):
      for i in data: 
        arr.append(i)
  except:
    print("No records registered. Please register!!")
    return False
  
  email = input("Enter your email: ")
  pwd = input("Enter your new password: ")
  
  for j, i in enumerate(data):
    if i["email"] == email :
      try:
        result = argon_pwd.verify(i["password"], pwd)
      except:
         result = False
         
      if result:
        print("Welcome back ", email)
        return
      else:
        print("Email or password incorrect!!")
        return
    if j == len(data):
      print("Email or password incorrect!!")

  
if __name__ ==  "__main__":
  op = 999
  while(op != 0):
    print("\n\n1 - Register \n2 - Login\n0 - Quit")
    op = input("Enter the desired option: ")

    if op == "1":
      email = input("Enter your email: ")
      pwd = input("Enter you r new password: ")
      
      if register(email, pwd):
        print("Success!!")
      else:
        print("Error!!")     
        
    elif op == "2" :
      login()
      
    if op == "0":
      break 
    
    if int(op) < 0 or int(op) > 2: 
      print("Please enter a valid option")
    
    