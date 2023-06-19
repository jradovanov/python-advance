rows, cols = [int(x) for x in input().split(",")]

matrix = []
for _ in range(rows):
    row = list(input())
    matrix.append(row)

mouse_r_position = -1
mouse_c_position = -1
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'M':
            mouse_r_position = row
            mouse_c_position = col
            break

cheese = sum(row.count('C') for row in matrix)
trap = sum(row.count('T') for row in matrix)

directions = []
trapped = False
while True:
    direction = input()
    if direction == 'danger':
        break
    directions.append(direction)

    new_row = mouse_r_position
    new_col = mouse_c_position

    if matrix[new_row][new_col] == 'T':
        trapped = True

    if trapped:
        break

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

    position = matrix[new_row][new_col]
    if position == '@':
        continue
    elif position == 'T':
        print("Mouse is trapped!")
        break
    elif position == 'C':
        cheese -= 1
        if cheese == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            matrix[mouse_r_position][mouse_c_position] = '*'
            matrix[new_row][new_col] = 'M'
            break
        else:
            matrix[mouse_r_position][mouse_c_position] = '*'
            matrix[new_row][new_col] = 'M'
    elif position == 'M':
        matrix[mouse_r_position][mouse_c_position] = '*'
        matrix[new_row][new_col] = 'M'

    mouse_r_position = new_row
    mouse_c_position = new_col

    if cheese > 0 and direction == 'danger':
        print("Mouse will come back later!")

for row in matrix:
    print("".join(row))
