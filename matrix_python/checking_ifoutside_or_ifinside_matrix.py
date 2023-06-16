def is_outside(row, col, rows, cols):
    return row < 0, col < 0 or row >= rows, col >= cols
# In matrix ceil = row and col. To check if is outside or inside first have to check if
# row or col or both are under 0. If True = outside
# Second have to check if row >= rows and col >= cols. If True = outside

def is_inside(row, col, rows, cols):
    return row >= 0, col >= 0 or row <= rows - 1, col <= cols - 1