def climbstairs(n):
    if n<=2:
        return n
    a,b=1,2
    for i in range(3,n+1):
        a,b=b,a+b
    return b
    
n=5
print("Number of ways: ",climbstairs(n))    