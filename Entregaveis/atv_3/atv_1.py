# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 03/10/2022 
# version ='1.9'
# Professor, não consegui nem sai da permutação inicial e ja estou a uns dias nisso
# ---------------------------------------------------------------------------

permutation_list = [58, 50, 42, 34, 26, 18,10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30,
                    22, 14, 6, 64, 56, 48 ,40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1,59, 51, 
                    43, 35, 27, 19, 11, 3, 61,53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15,
                    7]

def int_in_bit_64(num):
  return str(format(int(num), "064b"))

def int_in_bit_32(num):
  return str(format(int(num), "032b"))

def sub_key_generate(indicator ,key):
  if(indicator == 0):
    return key[0:4]
  else:
    return key[4:]
  

def shift_circular(message, displacement):
  l = list(message)
  saida = [0]*len(l)  
  
  for i in range(len(l)):
    saida[(i-displacement) % len(l)] = l[i]
  return saida
  
  
def initial_permutation(message):
  l = list(message)
  i = 0
  
  saida = [0]*len(l)
  for j in range(len(permutation_list)):
    saida[permutation_list[i]] = message[i]
  
  print(saida)
  new_message = ''.join(saida)
  return new_message

def encrypt(message, key):
  msg_in_bit_str = int_in_bit_64(message)
  msg_in_bit_str = initial_permutation(msg_in_bit_str)
  half_l = list(msg_in_bit_str[0:32])
  half_r = list(msg_in_bit_str[32:]) 
  
  int_half_l = int(''.join(half_l),2)
  int_half_r = int(''.join(half_r),2)
  
  equation = int_half_r + int(sub_key_generate(0,key), 2)
  
  xor = equation ^ int_half_l
  
  new_half_l = ''.join(half_r)
  new_half_r = int_in_bit_32(xor)
  
  res = int(''.join(new_half_l+new_half_r),2)

  return res

def decrypt(message, key):
  
  half_l = int_in_bit_64(message)[0:32]
  half_r = int_in_bit_64(message)[32:]
  
  new_half_r = half_l
  
  int_new_half_r = int(''.join(new_half_r),2)
  int_half_dir = int(''.join(half_r), 2)
  
  equation = int(int_new_half_r + int(sub_key_generate(0,key), 2))
  
  xor = equation ^ int_half_dir
  
  new_half_l = int_in_bit_32(xor)
  
  res = int(''.join(new_half_l+new_half_r),2)
  return res

if __name__ == "__main__" :
  msg = 139002343257
  key = 3
  msg_byte = bin(msg)
  
  print("Msg: ", msg, "\nKey: ", key)
  
  encrypt_message = encrypt(msg, bin(key))
  decrypted_message =  decrypt(encrypt_message, bin(key))
    
  print('Encrypted message:', encrypt_message)
  print("Decrypt message:",decrypted_message)
  print(msg == decrypted_message)