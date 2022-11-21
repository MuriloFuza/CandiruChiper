# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 10/11/2022 
# version ='1.0'
# Para utilizar a bib
# git clone git@github.com:lc6chang/ecc-pycrypto.git
# cd ecc-pycrypto
# pip3 install .
# ---------------------------------------------------------------------------

from ecc.curve import Curve25519
from ecc.key import gen_keypair
from ecc.cipher import ElGamal

def encryptMessage(message, key):
  cipher_elg = ElGamal(Curve25519)
  C1, C2 = cipher_elg.encrypt(message, key)
  return C1, C2, cipher_elg
    
def decryptMessage(privateKey, C1, C2, cipher_elg):
  
  message = cipher_elg.decrypt(privateKey, C1, C2)   
  return message
    
if __name__ ==  "__main__":
  
  # Insert your message here
  messageInit = b" Me de nota maxima Ewerton"
  print("Message: ", messageInit)
  
  # Generate keys
  # Murilo generates a pair of keys and sends it to Ewerton to encrypt his messages
  privateKey, publicKey = gen_keypair(Curve25519)
  
  C1,C2, cipher_elg = encryptMessage(messageInit, publicKey)
  
  print("\n\nThe points after encryption are: ", C1, C2)
  
  message = decryptMessage(privateKey, C1, C2, cipher_elg)
  
  print("\n\nThe decrypted message is: ", message, "\nIs she authentic?", message == messageInit)