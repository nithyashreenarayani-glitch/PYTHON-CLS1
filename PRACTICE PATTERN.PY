
#pyramid inverted

rows=int(input("Enter the row: "))   
for i in range(rows,0,-1):
    print(" "*(rows-i) + "*"*(2*i -1))

#diamond
    
rows=int(input("Enter the row: "))    
for i in range(1,rows+1):
    print(" "*(rows - i) + "*"*(2*i - 1))
for i in range(rows-1,0,-1):
    print(" "*(rows-i) + "*"*(2*i - 1))

#hollow sqr

rows=int(input("Enter the row: "))    
for i in range(rows):
    for j in range(rows):
        if(i==0 or i==rows-1 or j==0 or j==rows-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()          