# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 19/09/2022 
# version ='4.0'
# ---------------------------------------------------------------------------

from string import ascii_uppercase

alfabeto = list(ascii_uppercase)
def descobre_chave(mensagem, result):
  for i in range(26):
    print(mensagem, result)
    chave = i + 1
    if(mensagem == result):
      return i
    else:
      mensagem_cifrada = ""
      for i in mensagem:
        indice = ord(i)-65
        mensagem_cifrada += alfabeto[(indice-int(chave)) % len(alfabeto)] if i in alfabeto else i
      mensagem = mensagem_cifrada
      
mensagem = input('Mensagem cifrada: ')
esperada = input('Mensagem conhecida: ')
chavinha = descobre_chave(mensagem.upper(), esperada.upper())

print('Chave: ',chavinha)




