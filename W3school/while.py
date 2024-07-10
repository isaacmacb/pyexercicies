"""Imprima idesde que iseja menor que 6."""

i = 1
while i < 6:
    print(i)
    i += 1  

"""Break"""

i = 1
while i < 6 : 
    if i == 4 :
        break
        i += 1


"""Continue"""
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
    print(i)

"""Imprima uma mensagem quando a condição for falsa."""
 
i = 5

while i > 3:
   print(i)
   i+=1
else: 
   print("Essa é uma condição false")