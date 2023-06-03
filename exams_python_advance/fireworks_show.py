from collections import deque

effects = deque([int(x) for x in input().split(", ") if int(x) > 0])
power = [int(x) for x in input().split(", ") if int(x) > 0]
# print(effects, power)
palm = 0
willow = 0
crosse = 0
flag = False
while effects and power:
    if palm >= 3 and willow >= 3 and crosse >= 3:
        flag = True
        break

    current_effect = effects[0]
    current_power = power[-1]

    if (current_power + current_effect) % 3 == 0 and (current_power + current_effect) % 5 != 0:
        palm += 1
        effects.popleft()
        power.pop()
    elif (current_power + current_effect) % 5 == 0 and (current_power + current_effect) % 3 != 0:
        willow += 1
        effects.popleft()
        power.pop()
    elif (current_power + current_effect) % 3 == 0 and (current_power + current_effect) % 3 == 0:
        crosse += 1
        effects.popleft()
        power.pop()
    else:
        effects[0] -= 1
        a = effects.popleft()
        effects.append(a)

    if palm >= 3 and willow >= 3 and crosse >= 3:
        flag = True
        break

if flag:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crosse}")

# 90 points from 100