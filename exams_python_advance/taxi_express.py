from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxi_drivers = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxi_drivers:

    c = customers[0]
    t = taxi_drivers[-1]

    if c <= t:
        total_time += c
        customers.popleft()
        taxi_drivers.pop()

    else:
        taxi_drivers.pop()

if customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")

else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
