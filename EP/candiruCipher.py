


__author__ = "Murilo Fuza da Cunha"
__version__ = "1.0"
__email__ = "muriloacademix@gmail.com"
__status__ = "Prototype"


class CandiruCipher:
  def __init__(self) -> None:
    self.encryptingMessage = ''
    self.table = []
    self.encryptedMessage = ''
    self.keyGlobal = [4, 3, 1, 2, 5, 6, 7]
    self.keyFlow = 217
    self.messageRailFence = []
    self.messagePolyalphabetic = []
    self.messageFlow = []
    self.calc = 0
    self.positionLetter = { 
                           0: 'a',
                           1: 'b',
                           2: 'c',
                           3: 'd',
                           4: 'e',
                           5: 'f',
                           6: 'g',
                           7: 'h',
                           8: 'i',
                           9: 'j',
                           10 :'k',
                           11 :'l',
                           12 :'m',
                           13 :'n',
                           14 :'o',
                           15 :'p',
                           16 :'q',
                           17 :'r',
                           18 :'s',
                           19 :'t',
                           20 :'u',
                           21 :'v',
                           22 :'w',
                           23 :'x',
                           24 :'y',
                           25 :'z',
                           26 :' '
                           }
    self.table = [
      #A
      ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
       's','t', 'u', 'v','w', 'x', 'y', 'z', ' '],
      #B
      [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's','t', 'u', 'v','w', 'x', 'y', 'z'],
      #C
      ['z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
       'q', 'r', 's','t', 'u', 'v','w', 'x', 'y'],
      #D
      ['y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
       'p', 'q', 'r', 's','t', 'u', 'v','w', 'x' ],
      #E
      ['x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
       'o', 'p', 'q', 'r','s','t', 'u', 'v','w' ],
      #F
      ['w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
       'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v'],
      #G
      ['v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
       'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u'],
      #H
      ['u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t'],
      #I
      ['t','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s'],
      #J
      ['s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'],
      #k
      ['r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'],
      #L
      ['q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k', 'l', 'm', 'n', 'o', 'p'],
      #M
      ['p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k', 'l', 'm', 'n', 'o' ],
      #N
      ['o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k', 'l', 'm', 'n'],
      #O
      ['n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k', 'l', 'm' ],
      #P
      [ 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k', 'l' ],
      #Q
      ['l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j', 'k'],
      #R
      ['k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       'j'],
      #S
      ['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
       ],
      #T
      ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
       ],
      #U
      ['h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
       ],
      #V
      ['g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e', 'f', 
       ],
      #W
      ['f','g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd', 'e',  
       ],
      #X
      ['e', 'f','g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c', 'd',  
       ],
      #Y
      ['d','e', 'f','g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b', 'c',   
       ],
      #Z
      [ 'c', 'd','e', 'f','g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a', 'b',  
       ],
      #' '
      ['b', 'c', 'd','e', 'f','g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't','u','v', 'w' ,'x' ,'y', 'z' ,' ', 'a',  
       ],
      
    ]
  
  def railFenceCipher(self):
    self.calc = len(self.encryptingMessage) / len(self.keyGlobal)
    
    if(len(self.encryptingMessage) % len(self.keyGlobal) > 0):
      self.calc =int(self.calc) + 1

    self.calc = int(self.calc)
    
    limit = len(self.encryptingMessage) - 1
    j = 0
    
    # quebrar em vetores
    for i in range(self.calc):
      temp = []
      for k in range(len(self.keyGlobal)):
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
          key = self.keyGlobal[k]
          letter = self.messageRailFence[i][k]     
          
          # verificando quantas voltas é necessario
          if(key > len(temp)):
            guard = 0
            while(guard == 0):
              if(key > len(temp)):
                key = int(key / len(temp))
              else:
                guard = 1
               
          temp[key - 1] = letter
        guard += 1 
      self.messageRailFence[i] = temp
      
    guard = 0
    while(guard != -1):      
      if(len(self.messageRailFence[guard]) < len(self.keyGlobal)):
        limit = len(self.keyGlobal) - len(self.messageRailFence[guard])
        for i in range(limit):
           if(len(self.messageRailFence[guard]) < len(self.keyGlobal)):
             self.messageRailFence[guard].append("*")
        guard += 1
      else:
        guard += 1
      
      if(guard == len(self.messageRailFence)):
        guard = -1
                                   
    # concatenar o resultado final
    aux = ''
    count = len(self.messageRailFence[0])
    for l in self.messageRailFence[1:]:
      assert len(l) == count
    n = len(self.messageRailFence)
    final_len = n * count
    aux = [self.messageRailFence[i % n][int(i / n)] for i in range(final_len)]
    aux = "".join(aux)
    aux = aux.replace('*',"")
      
    self.messageRailFence = aux
    print("RailFence: ", self.messageRailFence)
    
    
  def polyalphabeticCipher(self):
  
    aux = []
    aux = list(self.messageRailFence)
    limit = len(aux)
    guard = 0
    
    while(guard < limit):
      for i in range(len(self.keyGlobal)):
        if(guard < limit):
          pos = list(self.positionLetter.keys())[list(self.positionLetter.values()).index(aux[guard])]
          self.messagePolyalphabetic.append(self.table[pos][self.keyGlobal[i]]) 
          guard += 1
  
    self.messagePolyalphabetic = "".join(self.messagePolyalphabetic)
    print("Polyalphabetic: ", self.messagePolyalphabetic)
    
    
  def flowCipher(self):
    final = []
    
    for c in self.messagePolyalphabetic:
      result = ord(c) ^ self.keyFlow
      print(chr(result))
      final.append(result)
    print(final)
  

  def encrypt(self, message, key):
    
    res = key.split(',')
    res = [int(numeric_string) for numeric_string in res]
    self.keyGlobal = res
    self.encryptingMessage = message
    
    self.railFenceCipher()
    self.polyalphabeticCipher()
    self.flowCipher()
  
  def decrypt(self, messageEncrypted):
    pass