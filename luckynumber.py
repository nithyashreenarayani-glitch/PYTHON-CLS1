n=int(input("enter a number: "))
sum=0
prod=1
temp=n
while temp>0:
    digit=temp%10
    sum+=digit
    prod*=digit
    temp//=10

if sum==prod:
    print(f"{n} It is a lucky number")  
else:
    print(f"{n} It is not a lucky number")      