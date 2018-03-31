value=int(input("enter the value"))
f=0
for i in range(1,value):
  if(value%i==0):
    f=i
if(f>1):
  print('The number is a composite number!')
elif(value==1):
  print('The number 1 is either composite or prime')
else:
  print('This is not a composite number!')
