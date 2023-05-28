'''
Matrix in python or multidimensional lists are lists in list.
Could be also dictionary in list, set in list, tuple in list etc.
Example:
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]] or if we want to visual matrix as a table:
Example:
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

Matrix can be 2D, 3D, 4D etc. Will work with 2D dimension
2D matrix has - rows and colones.
If you want to take 8 from matrix it will be - matrix[row][col] or in this matrix - matrix[2][1]
Important! - Always first index in matrix is a row, second one is a col

'''
# How to take 8 from matrix:
matrix = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
print(matrix[2][1])

# Hardcore matrix
matrix = []
for row in range(3):
    matrix.append([])
    for col in range(0, 5):
        matrix[row].append(col)
print(matrix)

# one line way to have a matrix
matrix = [[int(x) for x in input().split()] for row in range(3)]
print(matrix)

# row = int(input())
# matrix = []
#
# for _ in range(row):
#     inner_list = [int(x) for x in input().split(", ")]
#     matrix.append(inner_list)
# print(matrix)
# ===================================
# row = int(input())
# matrix = []
# for _ in range(row):
#     inner_list = []
#     data = input().split(", ")
#     for el in data:
#         inner_list.append(int(el))
#     matrix.append(inner_list)
# print(matrix)
# =================================
# row = int(input())
#
# matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]
#
# print(matrix)