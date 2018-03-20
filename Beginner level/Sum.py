list=[]
N=int(input("enter the N value"))
K=int(input("enter the K value"))
print("enter the values")
for i in range(N):
    value=int(input(""))
    list.append(value)
print("The result is",sum(list[0:K]))
