jobs = [int(x) for x in input().split(", ")]
index_to_find = int(input())

cycles = 0

for idx in range(len(jobs)):
    if jobs[idx] < jobs[index_to_find] or jobs[idx] == jobs[index_to_find]:
        cycles += jobs[idx]

print(cycles)