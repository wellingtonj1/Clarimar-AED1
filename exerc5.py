import random

def print_matrix(matrix, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end='   ')
        print()

# generates a matrix 5x5 with numbers between -10 and 10
matrix = []
row = 5
col = 5

for i in range(row):
    matrix.append([])
    for j in range(col):
        matrix[i].append(random.randint(-10, 10))
        
# prints the matrix 
print_matrix(matrix, row, col)
    
# count how many elements are negative in the matrix
negative = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] < 0:
            negative += 1
print("\nThere are", negative, "negative numbers in the matrix")

# set the negative values to 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] < 0:
            matrix[i][j] = 0
print("\nMatrix with negative values seted to 0")
print_matrix(matrix, row, col)
            
# sum the positive values in the matrix
positive_sum = 0    
qty_positives = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] > 0:
            positive_sum += matrix[i][j]
            qty_positives += 1
print("\nThe sum of the positive values is", positive_sum)

# calculate average of the positive values in the matrix
positive_average = positive_sum / qty_positives
print("The average of the positive values is", positive_average)

