arr=[1,2,3,4,5,6,7,8,9]
matrix=[[arr[0],arr[1],arr[2]],
        [arr[3],arr[4],arr[5]],
        [arr[6],arr[7],arr[8]]]

diagonal=[matrix[i][i] for i in range(0,3)]
diagonal_sum=sum(diagonal)
print("diagonal: ",diagonal)
print("diagonal an its sum:",diagonal_sum)