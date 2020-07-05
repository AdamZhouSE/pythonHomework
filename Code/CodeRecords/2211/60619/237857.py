l = input().split()
ladies = int(l[0])
interests = int(l[1])
name = []
for i in range(ladies):
    li = input().split()
    if i == 0:
        name.append(li[0])
    else:
        name.append(li[0] + name[int(li[1])-1])
for i in range(interests):
    string = input()
    numbers = 0
    for j in name:
        if j.startswith(string):
            numbers += 1
    print(numbers)