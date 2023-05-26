row = int(input())
matrix = []
for _ in range(row):
    inner_list = [int(x) for x in input().split(", ")]
    even_numbers = []
    for el in inner_list:
        if el % 2 == 0:
            even_numbers.append(el)
    matrix.append(even_numbers)
print(matrix)
