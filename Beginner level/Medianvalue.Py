list=[]
num=int(input("enter the count value"))
for i in range(num):
  value=int(input(" "))
  list.append(value)
total=sum(list)
print("the median is ",total/num)
