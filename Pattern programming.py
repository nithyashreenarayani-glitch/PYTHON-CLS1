#Inverted right angle 
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("*" * i)

#Pyramid
    
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1)) 

#Diamond
    
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

#Inverted pyramid 
    
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

