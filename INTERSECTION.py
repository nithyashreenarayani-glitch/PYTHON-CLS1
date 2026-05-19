def intersection(num1,num2):
    num2_copy=num2.copy()
    result=[]
    for i in num1:
        if i in num2_copy:
            result.append(i)
            num2_copy.remove(i)
    return result

n1=[1,2,2,3]   
n2=[2,2]   
print(intersection(n1,n2))
z1=[4,5,9,5,4]  
z2=[5,4]
print(intersection(z1,z2))