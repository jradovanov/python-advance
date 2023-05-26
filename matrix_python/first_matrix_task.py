'''
Write a program that reads a matrix from the console and prints:
• The sum of all numbers in the matrix
• The matrix itself
On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
On the next rows, you will
get elements for each column separated by a comma and a space ", ".
'''
# first have to read number of rows and colones
# in this task using comprehension to read and change elements of the list in integers
rows, colones = [int(x) for x in input().split(", ")]
# One variable for new matrix
matrix = []
# variable to keep sums
sum_matrix = 0
# for loops to read elements of each row
for _ in range(rows):
    # variable to keep elements of every row using comprehension to change elements to integers
    inner_list = [int(x) for x in input().split(", ")]
    # adding the sum of elements in current row to sum_matrix variable
    sum_matrix += sum(inner_list)
    # appending current inner_list to matrix
    matrix.append(inner_list)
# printing both variables
print(sum_matrix)
print(matrix)

# variant without comprehension
rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    numbers_as_string = input().split(", ")
    inner_list = []

    for n in numbers_as_string:
        inner_list.append(int(n))
    matrix.append(inner_list)

sum_rows_cols = 0
for row in range(rows):
    for col in range(cols):
        sum_rows_cols += matrix[row][col]

print(sum_rows_cols)
print(matrix)
