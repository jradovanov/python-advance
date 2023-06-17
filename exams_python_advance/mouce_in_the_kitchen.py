rows, cols = [int(x) for x in input().split(",")]
cupboards = []

mouse_pos = [0, 0]
cheese = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    cupboards.append(list(input()))
    if "M" in cupboards[row]:
        mouse_pos = [row, cupboards[row].index("M")]
        cupboards[mouse_pos[0]][mouse_pos[1]] = "*"
    if "C" in cupboards[row]:
        cheese += cupboards[row].count("C")

while True:
    command = input()
    if command == "danger":
        print(f"Mouse will come back later!")
        break

    n_row, n_col = mouse_pos[0] + directions[command][0], mouse_pos[1] + directions[command][1]

    if n_row < 0 or n_col < 0 or n_row >= rows or n_col >= cols:
        print(f"No more cheese for tonight!")
        break

    next_position = cupboards[n_row][n_col]

    if next_position == "@":
        continue

    mouse_pos = [n_row, n_col]

    if next_position == "C":
        cheese -= 1
        if cheese == 0:
            print(F"Happy mouse! All the cheese is eaten, good night!")
            break
        cupboards[n_row][n_col] = "*"

    elif next_position == "T":
        print(F"Mouse is trapped!")
        break

cupboards[mouse_pos[0]][mouse_pos[1]] = "M"
[print(*row, sep="") for row in cupboards]