from argon2 import PasswordHasher

argon_pwd = PasswordHasher() 

pwd = 'murilo@'

pwd_hash = argon_pwd.using(rounds=4).hash(pwd)

print(pwd_hash)

if(argon_pwd.verify("pwd", pwd_hash)):
  print("True")
else:
  print("False")