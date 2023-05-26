# the python way to have a matrix with zeros:
matrix = [[0 for col in range(6)] for row in range(3)]
print(matrix)


# the python way to have a matrix with numbers:
matrix = [[number for number in range(1, 7)] for row in range(3)]
print(matrix)

# flattening matrix means to unpack the matrix:
matrix = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
# raising new list named flatten
flatten = []
# now have to iterate all matrix elements - main and nested
for row in range(len(matrix)): # main
    for col in range(len(matrix[row])): # nested
        # raising variable presented current element
        current_element = matrix[row][col]
        # every current element going to the flatten list
        flatten.append(current_element)
# printin flatten list
print(flatten)
'''
row = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(row)] # normal matrix
matrix = [int(x) for _ in range(row) for x in input().split(", ")] # flattening
print(matrix)
'''