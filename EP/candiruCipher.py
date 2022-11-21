


__author__ = "Murilo Fuza da Cunha"
__version__ = "1.0"
__email__ = "muriloacademix@gmail.com"
__status__ = "Prototype"


class CandiruCipher:
  def __init__(self) -> None:
    self.encryptingMessage = ''
    self.table = []
    self.encryptedMessage = ''
    self.keyRailFence = [4, 3, 1, 2, 5, 6, 7]
    self.messageRailFence = []
    self.calc = 0
  
  def railFenceCipher(self):
    self.calc = len(self.encryptingMessage) / 7
    
    if(len(self.encryptingMessage) % 7 > 0):
      self.calc =int(self.calc) + 1

    self.calc = int(self.calc)
    
    limit = len(self.encryptingMessage) - 1
    j = 0
    
    # quebrar em vetores
    for i in range(self.calc):
      temp = []
      for k in range(len(self.keyRailFence)):
        if(j <= limit):
          temp.append(self.encryptingMessage[j])
          j += 1
      self.messageRailFence.append(temp)
      
    # colocar na ordem encriptada
    guard = 0
    for i in range(len(self.messageRailFence)):
      temp = [0]*len(self.messageRailFence[i])
      for k in range((len(self.messageRailFence[i]))):
        if(guard <= limit):
          key = self.keyRailFence[k]
          letter = self.messageRailFence[i][k]          
          temp[key - 1] = letter
        guard += 1 
      self.messageRailFence[i] = temp
      
    # concatenar o resultado final
    temp = ["*"]*len(self.messageRailFence[i])
    for i in range(len(self.messageRailFence)):
      for k in range((len(self.messageRailFence[i]))):
        temp[k] += self.messageRailFence[i][k]
    temp = "".join(temp)
    
    # removendo os * 
    b = '*'
    for i in range(0,len(b)):
      temp = temp.replace(b[i],"")
      
    self.messageRailFence = temp        
    print(self.messageRailFence)

  def encrypt(self, message):
    self.encryptingMessage = message
    self.railFenceCipher()
    pass
  
  def decrypt(self, messageEncrypted):
    pass