value=int(input("enter the value"))
value1=value
temp = 0  
while value1 > 0:  
   digit = value1 % 10  
   temp+= digit ** 3  
   value1 //= 10
if (value==temp):
  print("the given number is amstrong")
else:
  print("The given number is not amstrong")
