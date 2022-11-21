# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 18/10/2022 
# version ='1.0'
# ---------------------------------------------------------------------------

import hashlib
import hmac

iterations = 10000
key = "lUNj6mWIFOxr219G2nV1lw"

def sendMessage(message, integrity_hmac):
  
  verifyIntegrityMessage = hmac.new(key.encode(), message.encode(),
                               hashlib.sha256).hexdigest()
  
  if verifyIntegrityMessage == integrity_hmac:
    print("your message reached its destination correctly!")
    print("\nYour message is: ", message)
  else:
    print("Oops, your message has been changed!")

if __name__ == "__main__":
  message = input("Digite a mensagem: ")
  
  integrityMessage = hmac.new(key.encode(), message.encode(),
                               hashlib.sha256).hexdigest()
  
  sendMessage(message, integrity_hmac=integrityMessage) 