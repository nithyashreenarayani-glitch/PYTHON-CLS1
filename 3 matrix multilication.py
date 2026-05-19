A = [[1, 2],
     [3, 4],
     [4, 6]]

B = [[2, 0],
     [1, 2],
     [6, 7]]

C = [[1, 1],
     [0, 1],
     [8, 5]]

# 2️⃣ Function to multiply two matrices
def multiply(X, Y):
    result = [[0, 0],
              [0, 0]]
    for i in range(2):          # 2 rows
        for j in range(2):      # 2 columns
            for k in range(2):  # multiply row*column
                result[i][j] += X[i][k] * Y[k][j]
    return result

# 3️⃣ Multiply A and B first
AB = multiply(A, B)

# 4️⃣ Multiply result (AB) with C
ABC = multiply(AB, C)

# 5️⃣ Print all results
print("Matrix A:", A)
print("Matrix B:", B)
print("Matrix C:", C)
print("A x B =", AB)
print("A x B x C =", ABC)