#CSES PROBLEM: epetition solution in python

x = input()
counter = 1
longestsequences = 0

if len(x) == 1:
  print(1) 
else:
  for i in range(len(x)-1):
  #if len(x) == 1:
    #print(1)
    #break
      if x[i] == x[i+1]:
        counter +=1
    #if counter > longestsequences:
      #longestsequences = counter
      else:
        if counter > longestsequences:
          longestsequences = counter
        counter = 1


if counter > longestsequences:
    longestsequences = counter
print(longestsequences)

  
