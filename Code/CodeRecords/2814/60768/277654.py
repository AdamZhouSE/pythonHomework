customer = int(input())
line = input().split(' ')
line = [int(x) for x in line]
line.sort()
satisfied = []
i = 0
while i < len(line):
    if line[i] >= sum(satisfied):
        satisfied.append(line[i])
        line.pop(i)
    else:
        i += 1

print(len(satisfied))