list=[]
n=int(input("enter the n value"))
k=int(input("enter the k value"))
print(" enter the n values")
for i in range(n):
  values=int(input(" "))
  list.append(values)
if(k in list):
  print('the given number is available in the list')
else:
  print(" the given number is not available in the list")
