# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 07/11/2022 
# version ='1.0'
# Utilizei 1024 de tamanho da chave pq maiores demora muito
# ---------------------------------------------------------------------------

import rsa

def keyGenerator(user):
  (PublicKey, PrivateKey) = rsa.newkeys(1024)
  nameFile = "./sharedKey%s.pem" % user
  nameFileP = "./privateKey%s.pem" % user
  with open(nameFile, 'wb') as file:
        file.write(PublicKey.save_pkcs1('PEM'))
  with open(nameFileP, 'wb') as file:
        file.write(PrivateKey.save_pkcs1('PEM'))
        
def loadKey(user):
  nameFile = "./sharedKey%s.pem" % user
  nameFileP = "./privateKey%s.pem" % user
  with open(nameFile, 'rb') as file:
      PublicKey = rsa.PublicKey.load_pkcs1(file.read())
  with open(nameFileP, 'rb') as file:
      PrivateKey = rsa.PrivateKey.load_pkcs1(file.read())
  return PublicKey, PrivateKey
  
def encryptMessage(message, key):
  encryptedMessage = rsa.encrypt(message.encode('ascii'), key)
  return encryptedMessage

def decryptMessage(message, eMessage, key):
  
  try:
    decryptedMessage = rsa.decrypt(eMessage, key).decode('ascii')
    print("Message decrypted: ", decryptedMessage)
    
    if(message == decryptedMessage):
      print("\nAuthentic message")
    else: 
      print("\nMessage has been compromised")
  except:
    print("\nUnable to decrypt the message with this key!")      
    

    
if __name__ ==  "__main__":
  
  message = input("Message: ")
  
  keyGenerator('Murilo')
  keyGenerator('Ewerton')
  
  print("\nMurilo receives Ewerton public key")
  sKey, pKey = loadKey('Ewerton')
  print("\nKey received: ", sKey)
  
  messageEncrypted = encryptMessage(message, sKey); 
  print("\n\nMurilo encrypts the message with Ewerton public key: ", messageEncrypted)
  
  print("\n\nEwerton decrypts with his private key")
  decryptMessage(message, messageEncrypted, pKey)
  