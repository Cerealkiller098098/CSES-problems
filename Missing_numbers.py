x = int(input())
list = []

#assuming the inputs are intergers
#for loop to input the numbers
for i in range(x-1):
  y = int(input())
  list.append(y)


#finds the missing number
counter = range(1,x+1)
for i in counter:
  if i not in list:
    print(i)
