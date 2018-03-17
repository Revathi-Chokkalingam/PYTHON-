list=[]
value=int(input("choose the count u want"))
for i in range(value):
  num=int(input(" "))
  list.append(num)
print("The minimum value among these numbers are",min(list))
