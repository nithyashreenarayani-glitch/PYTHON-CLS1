n=int(input("enter a number: "))
num_str=str(n)
length=len(num_str)
if(len(num_str)%2==0):
    first_half=int(num_str[0:length//2])
    second_half=int(num_str[length//2:])
    total=first_half+second_half
    tot=total*total
    if(tot==n):
        print(f"It is a tech number")
    else:
        print(f"Not a tech number")    