

def fun(X):
  return (X * 3)%8

for i in range(20):
  print("i = ",i, "Hash = ",fun(i))