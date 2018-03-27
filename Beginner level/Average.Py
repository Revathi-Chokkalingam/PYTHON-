list=[]
value1=int(input("enter the count value"))
print("enter the values")
for i in range(value1):
  value=int(input(" "))
  list.append(value)
sum=sum(list)
average=sum/value1
print("The average value is ",average)
