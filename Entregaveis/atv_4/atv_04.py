# -*- coding: utf-8  
#----------------------------------------------------------------------------
# Created By  : Murilo Fuza da Cunha  
# Created Date: 09/10/2022 
# version ='1.2'
# Professor como eu faltei na aula por estar doente acredito que seja isso que é para entregar
# ---------------------------------------------------------------------------

Pa = [1,0,4,2,3,5]

def perm(input_array):
  output_array = [0]*len(input_array)
  for i in range(len(input_array)):
    output_array[Pa[i]] = input_array[i] 
  return output_array
  
def shift_circular_right(input_array,displacement):
  output_array = [0]*len(input_array)
  for i in range(len(input_array)):
    output_array[(i+displacement)%len(input_array)] = input_array[i]
  return output_array

def hash_atv_4(input_array):
  h = 0
  for i in range(len(input_array)):
    h = h ^ input_array[i]
  return h

input_array = [1,0,1,0,1,0]
print(input_array)
permuted_value = perm(input_array)
shift_circular_right = shift_circular_right(permuted_value,3)
final_hash = hash_atv_4(shift_circular_right)

print("Input array hash: ", final_hash)
