m=2
n=2
m2=2
n2=2
 
 
mat = []
line = []
mattrans = []
matsum = []
matmul = []
 
print("Enter Elements of the matrix : ")
 
for i in range(0, m):
	line = []
	for j in range(0, n):
		line.append(int(input()))
	mat.append(line)
 
for i in range(0, m):
	mattrans.append([])
	for j in range(0, n):
		mattrans[i].append(0)
		mattrans[i][j] = mat[j][i]
 
 
for i in range(0, m):
        matsum.append([])
        for j in range(0, n):
                matsum[i].append(0)
                matsum[i][j] = mat[i][j] + mattrans[i][j]
 
for i in range(0, m):
	matmul.append([])
	for j in range(0, n):
		matmul[i].append(0)
		sum = 0
		for k in range(0, m):
			prod = mat[i][k] * mattrans[k][j]
			sum += prod
		matmul[i][j] = sum
 
 
print("\nMatrix : ")
for i in range(m):
	print(mat[i])
 
print("\nTranspose Of The Matrix : ")
for i in range(m):
        print(mattrans[i])
 
print("\nSum Of Matrices Matrix : ")
for i in range(m):
        print(matsum[i])
 
print("\nProduct Of Matrix : ")
for i in range(m):
        print(matmul[i])
