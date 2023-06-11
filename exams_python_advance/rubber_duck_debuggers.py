from collections import deque

times = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

duck_dict = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while times and tasks:
    time = times.popleft()
    task = tasks.pop()
    result = time * task
    if 181 <= result <= 240:
        duck_dict["Small Yellow Rubber Ducky"] += 1
        continue

    elif 121 <= result <= 180:
        duck_dict["Big Blue Rubber Ducky"] += 1
        continue

    elif 61 <= result <= 120:
        duck_dict["Thor Ducky"] += 1
        continue

    elif 0 <= result <= 60:
        duck_dict["Darth Vader Ducky"] += 1
        continue

    elif result > 240:
        tasks.append(task - 2)
        times.append(time)
        continue

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in duck_dict.items():
    print(f"{key}: {value}")
