def removedigits(num,k):
    stack=[]
    for digits in num:
        while(k>0 and stack and stack[-1]>digits):
            stack.pop()
            k-=1
        stack.append(digits) 

    while(k>0):
        stack.pop()    

    result="".join(stack).strip('0')
    return result if result else '0'  

print(removedigits("1432219",3))    
print(removedigits("10200388",1)) 


