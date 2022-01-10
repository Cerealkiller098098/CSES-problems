def Permutation(number):
  if number == 1 or number == 2 or number == 3:
    print("No solution")
  list = []
  for i in range(number,0,-2): 
    list.append(i)
  for j in range(number-1,0,-2):
    list.append(j)
  print(list)

