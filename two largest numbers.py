arr=list(map(int,input("enter a number: ").split()))
l1=max(arr)
arr.remove(l1)
l2=max(arr)

print("The first largest number: ",l1)
print("The second largest numbe is: ",l2)