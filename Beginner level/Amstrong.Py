low= int(input("Enter lower range: "))
up = int(input("Enter upper range: "))
 
for i in range(low,up + 1):
   value = 0
   t = i
   while t > 0:
       digit = t % 10
       value += digit ** 3
       t //= 10
   if i == value:
       print(i)

