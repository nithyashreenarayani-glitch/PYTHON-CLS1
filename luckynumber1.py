def is_lucky(n):
    if n<0:
        n=-(n)
    sum=0
    prod=1
    temp=n
    if temp==0:
        sum=0
        prod=0
    while temp>0:
        digit=temp%10
        sum+=digit
        prod*=digit
        temp//=10
    return sum==prod    

n=int(input("enter a number: "))   
if is_lucky(n):
    print(f"{n} is a lucky number")
else:
    print(f"{n} is not a lucky number")         

