list=[]
n=int(input("enter the n elements"))
for i in range(0,n):
     number=int(input(""))
     list.append(number)
list.sort()
print("Largest element is:",list[n-1])
