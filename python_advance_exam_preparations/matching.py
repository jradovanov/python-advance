from collections import deque

males = [int(male) for male in input().split()]
females = deque(int(female) for female in input().split())

matches = 0

while True:
    if not males or not females:
        break

    current_male = males[-1]
    current_female = females[0]

    if current_male <= 0:
        males.pop()
        continue
    if current_female <= 0:
        females.popleft()
        continue

    if current_male % 25 == 0:
        males.pop()
        if not males:
            break
        males.pop()
        continue
    if current_female % 25 == 0:
        females.popleft()
        if not females:
            break
        females.popleft()
        continue

    if current_male == current_female:
        males.pop()
        females.popleft()
        matches += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f'Matches: {matches}')

if males:
    print(f"Males left: {', '.join(str(male) for male in reversed(males))}")
else:
    print('Males left: none')

if females:
    print(f"Females left: {', '.join(str(female) for female in females)}")
else:
    print('Females left: none')