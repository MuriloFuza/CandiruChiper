# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 20/09/2022 
# version ='1.3'
# cada () é um passo 
# ---------------------------------------------------------------------------

from math import sqrt

def encrypt(message, key):
  encrypting = bin(((((((message + key) - 3 ) * key) ^ 7) * key) ** 2))
  return encrypting

def decrypt(encrypted_message, key):
  decrypting = (((((int((sqrt(int(encrypted_message, 2))) / key)) ^ 7 ) / key) + 3) - key)
  return decrypting

if __name__ == "__main__":
  msg = 12
  key = 6
  
  print("*** Cifra desenvolvida em sala de aula ***")
  print("Msg: ", msg, "\nKey: ", key)
  
  encrypted_message = encrypt(msg, key)
  decrypted_message = decrypt(encrypted_message, key)
  
  print("\nEncrypted text: ", encrypted_message, "\nDecrypted text: ", decrypted_message)