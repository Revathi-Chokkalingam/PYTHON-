list=[]
number=int(input('enter the n value'))
value=int(input('enter the k value'))
for i in range(number):
    n=int(input(" "))    
    list.append(n)
if(value in list):
    print('yes')
else:
    print('no')
