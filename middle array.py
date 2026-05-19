arr=list(map(int,input("\nenter numbers separated by spaces\n").split()))
arr.sort()
print(arr)
middle_index=len(arr)//2
middle_number=arr[middle_index]
print(middle_number)