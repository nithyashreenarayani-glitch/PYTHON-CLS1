num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    digits=temp%10
    sum+=digits
    temp=temp//10
print("Sum of digits",sum)   