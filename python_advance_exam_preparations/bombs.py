#
from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

datura = 0
cherry = 0
smoke = 0
finish = False

while bomb_effects and bomb_casings:
    current_material = bomb_effects[0] + bomb_casings[-1]

    if current_material == 40:
        datura += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_material == 60:
        cherry += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif current_material == 120:
        smoke += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if datura == 3 and cherry == 3 and smoke == 3:
        finish = True
        break

if finish:
    print("Bene! You have successfully filled the bomb pouch!")
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
    print(f"Cherry Bombs: {cherry}")
    print(f"Datura Bombs: {datura}")
    print(f"Smoke Decoy Bombs: {smoke}")
else:
    print("You don't have enough materials to fill the bomb pouch.")
    if not bomb_effects:
        print("Bomb Effects: empty")
    else:
        print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
    if not bomb_casings:
        print("Bomb Casings: empty")
    else:
        print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
    print(f"Cherry Bombs: {cherry}")
    print(f"Datura Bombs: {datura}")
    print(f"Smoke Decoy Bombs: {smoke}")

# from collections import deque
#
# bomb_effects = deque([int(x) for x in input().split(", ")])
# bomb_casings = [int(x) for x in input().split(", ")]
#
# datura = 0
# cherry = 0
# smoke = 0
# finish = False
# while bomb_effects and bomb_casings:
#     current_material = bomb_effects[0] + bomb_casings[-1]
#     if current_material == 40:
#         datura += 1
#         bomb_effects.popleft()
#         bomb_casings.pop()
#     elif current_material == 60:
#         cherry += 1
#         bomb_effects.popleft()
#         bomb_casings.pop()
#     elif current_material == 120:
#         smoke += 1
#         bomb_effects.popleft()
#         bomb_casings.pop()
#     else:
#         bomb_casings[-1] -= 5
#
#     if datura == 3 and cherry == 3 and smoke == 3:
#         finish = True
#         break
# if finish:
#     print("Bene! You have successfully filled the bomb pouch!")
#     print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
#     print(f"Casings: {', '.join(str(x) for x in bomb_casings)}")
#     print(f"Bombs: {cherry}")
#     print(f"Bombs: {datura}")
#     print(f"Decoy Bombs: {smoke}")
# else:
#     print("You don't have enough materials to fill the bomb pouch.")
#     if not bomb_effects:
#         print(f"Bomb Effects: empty")
#     else:
#         print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
#     if not bomb_casings:
#         print(f"Bomb Casings: empty")
#     print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
#     print(f"Cherry Bombs: {cherry}\nDatura Bombs: {datura}\nSmoke Decoy Bombs: {smoke}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
