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