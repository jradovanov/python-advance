# Входни данни
rows, cols = [int(x) for x in input().split(",")]
# map(int, input().split(","))
matrix = [list(input()) for _ in range(rows)]


# Намиране на позицията на мишката
mouse_row_position, mouse_col_position = None, None
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'M':
            mouse_row_position, mouse_col_position = row, col
            break

# Изпълнение на командите
cheese_count = sum(row.count('C') for row in matrix)
trap_count = sum(row.count('T') for row in matrix)
directions = []
while True:
    direction = input()
    if direction == 'danger':
        break
    directions.append(direction)

    new_row, new_col = mouse_row, mouse_col

    if direction == 'up':
        new_row -= 1
    elif direction == 'down':
        new_row += 1
    elif direction == 'left':
        new_col -= 1
    elif direction == 'right':
        new_col += 1

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        print("No more cheese for tonight!")
        break

    cell_value = matrix[new_row][new_col]
    if cell_value == '@':
        continue
    elif cell_value == 'T':
        print("Mouse is trapped!")
        break
    elif cell_value == 'C':
        cheese_count -= 1
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[mouse_row][mouse_col] = '*'
            matrix[new_row][new_col] = 'M'
            break
        else:
            matrix[mouse_row][mouse_col] = '*'
            matrix[new_row][new_col] = 'M'
    elif cell_value == 'M':
        matrix[mouse_row][mouse_col] = '*'
        matrix[new_row][new_col] = 'M'

    mouse_row, mouse_col = new_row, new_col

if cheese_count > 0 and direction == 'danger':
    print("Mouse will come back later!")

# Извеждане на финалната матрица
for row in matrix:
    print("".join(row))
