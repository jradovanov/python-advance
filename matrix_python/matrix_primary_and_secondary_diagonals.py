rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

primary = []
secondary = []

for r in range(rows):
    primary.append(matrix[r][r])
    secondary.append(matrix[r][rows - 1 - r])

print(primary)
print(secondary)

# unpacked

print(", ".join(str(x) for x in primary))
print(", ".join(str(x) for x in secondary))
