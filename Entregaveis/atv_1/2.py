# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 19/09/2022 
# version ='8.0' - Esse eu passei sufoco kkk
# ---------------------------------------------------------------------------

from string import ascii_uppercase

alfabeto = str(ascii_uppercase)

def cifrar(mensagem, chave):
  mensagem_cifrada = ""
  i=0
  
  for letra in mensagem:
    soma = alfabeto.find(letra) + alfabeto.find(chave[i % len(chave)])
    indice = int(soma) % len(alfabeto)
    mensagem_cifrada += str(alfabeto[indice])
    i += 1
  
  return mensagem_cifrada

def descifrar(mensagem, chave):
  mensagem_cifrada = ""
  i=0
  
  for letra in mensagem:
    soma = alfabeto.find(letra) - alfabeto.find(chave[i % len(chave)])
    indice = int(soma) % len(alfabeto)
    mensagem_cifrada += str(alfabeto[indice])
    i += 1
  
  return mensagem_cifrada

mensagem = input('Digite a mensagem: ')
chave = input('Digite a chave: ')

mensagem = mensagem.upper()
chave = chave.upper()

cifrada = cifrar(mensagem, chave)

print('Mensagem cifrada: ', cifrada)
print('Mensagem descifrada: ', descifrar(cifrada, chave))