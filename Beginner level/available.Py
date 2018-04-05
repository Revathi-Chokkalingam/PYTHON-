list=[]
number=int(input('enter the value'))
v1=int(input('enter the min value'))
v2=int(input('enter the max value'))
for i in range(v1,v2+1):
  list.append(i)
if(number in list):
  print('the given number is available in the interval')
else:
  print('the given number is not availble in the interval')
