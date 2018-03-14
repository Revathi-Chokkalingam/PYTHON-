list=[]
n=10
print("enter the 10 elements") 
for i in range(0,n):
     number=int(input("Enter element:"))
     list.append(number)
list.sort()
print("Largest element is:",list[n-1])
