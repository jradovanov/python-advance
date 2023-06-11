from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

boxes = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_toys = {}

while materials and magic_level:

    material = materials.pop()
    magic = magic_level.popleft()

    result = material * magic

    if result in boxes:
        toys = boxes[result]
        if toys not in crafted_toys:
            crafted_toys[toys] = 1
        else:
            crafted_toys[toys] += 1

    elif result < 0:
        materials.append(material + magic)

    elif result > 0:
        materials.append(material + 15)

    else:
        if material == 0 and magic == 0:
            continue

        elif material == 0:
            magic_level.appendleft(magic)

        else:
            materials.append(material)

if "Doll" in crafted_toys and "Wooden train" in crafted_toys \
        or "Teddy bear" in crafted_toys and "Bicycle" in crafted_toys:
    print("The presents are crafted! Merry Christmas!")

else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic_level:
    print(f"Magic left: {', '.join([str(x) for x in magic_level])}")

for toy, count in sorted(crafted_toys.items()):
    print(f"{toy}: {count}")

# 10 -5 20 15 -30 10
# 40 60 10 4 10 0