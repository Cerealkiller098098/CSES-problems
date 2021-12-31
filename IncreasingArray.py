y = int(input())
# you wont be using this y
x = list(map(int,input().split()))

counter = 1
biggestgap = 0
index1 = 0
index2 = 0
output = 0

for i in x:
  if counter == len(x):
    break
  if i < x[counter]:
    counter += 1
    continue
  else:
    index1 = counter -1
    while x[counter] < i: 
      if i - x[counter] > biggestgap:
        biggestgap = i - x [counter]
        index2 = counter
        counter += 1 
    if output < (biggestgap+(index2-index1)):
      output =(biggestgap+(index2-index1))
print(output)


    
    
  

  
    
