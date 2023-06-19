from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])

challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()

    result = tool * substance
    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(tool + 1)
        if substance - 1 > 0:
            substances.append(substance - 1)

if len(challenges) > 0:
    print("Harry is lost in the temple. Oblivion awaits him.")
    if tools:
        print(f"Tools: {', '.join(str(x) for x in tools)}")
    if substances:
        print(f"Substances: {', '.join(str(x) for x in substances)}")
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")

else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print(f"Tools: {', '.join(str(x) for x in tools)}")
    if substances:
        print(f"Substances: {', '.join(str(x) for x in substances)}")


# from collections import deque
#
# tools = deque([int(x) for x in input().split()])
# substances = [int(x) for x in input().split()]
#
# challenges = [int(x) for x in input().split()]
#
# while tools and substances and challenges:
#     tool = tools.popleft()
#     substance = substances.pop()
#
#     result = tool * substance
#     for el in challenges:
#         if result == el:
#             challenges.remove(el)
#         else:
#             tools.append(tool + 1)
#             if substance -1 > 0:
#                 substances.append(substance - 1)
#             else:
#                 continue
#
# if len(challenges) > 0:
#     print("Harry is lost in the temple. Oblivion awaits him.")
#     if tools:
#         print(f"Tools: {', '.join(str(x) for x in tools)}")
#     if substances:
#         print(f"Substances: {', '.join(str(x) for x in substances)}")
#     print(f"Challenges: {', '.join(str(x) for x in challenges)}")
#
# else:
#     print("Harry found an ostracon, which is dated to the 6th century BCE.")
#     if tools:
#         print(f"Tools: {', '.join(str(x) for x in tools)}")
#     if substances:
#         print(f"Substances: {', '.join(str(x) for x in substances)}")