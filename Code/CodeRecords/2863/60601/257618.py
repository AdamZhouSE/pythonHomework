line = input().split(' ')
n = int(line[0])
high = int(line[1])
people = list(map(int,input().split(' ')))
result = len(people)
for i in people:
    if i>high:
        result = result + 1
print(result)