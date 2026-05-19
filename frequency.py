num=input("enter number: ")
freq={}
for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

for key,value in freq.items():
    print(key," : ",value)
