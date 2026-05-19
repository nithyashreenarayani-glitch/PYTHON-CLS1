#n=int(input("enter a number: "))


def intersect(n1,n2):
    result=[]
    n2_copy=n2.copy()
    for i in n1:
        if i in n2_copy:
            result.append(i)
            n2_copy.remove(i)
        return result
n1=[1,2,2,4]        
n2=[1,2]
print(intersect(n1,n2))