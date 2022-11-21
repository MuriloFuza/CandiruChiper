# -*- coding: utf-8
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha
# Created Date: 25/09/2022
# version ='1.3'
# Cipher  Cypher-Block Chaining (CBC)
# ---------------------------------------------------------------------------

from math import sqrt

def encrypt(message, key):
  iv = 3
  n = 2
  for i in range(n):
    equation = (((message + key) - iv) * iv)
    iv = iv ** 2
  encrypted_message = bin(equation)
  return encrypted_message

def decrypt(message, key):
  n = 2
  iv = (3*3)**n
  msg = int(message, 2)
  for i in range(n):
    equation = (((msg / iv) - key) + iv )
    iv = sqrt(iv)
  decrypt_message = equation
  return decrypt_message

if __name__ == "__main__" :
  msg = 365
  key = 3
  
  print("Msg: ", msg, "\nKey: ", key)
  
  encrypt_message = encrypt(msg, key)
  
  print('Encrypted message:', encrypt_message)
  print("Decrypt message:", decrypt(encrypt_message, key))