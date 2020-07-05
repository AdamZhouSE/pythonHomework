cout = input()
for i in range(int(cout)):
    t = input()
    initial = input()
    array = initial.split(" ")
    character = []
    times = []
    for i in array:
        if i not in character:
            character.append(i)
            times.append(1)
        else:
            times[character.index(i)] += 1
    haveMost = False
    for j in range(len(times)):
        if int(times[j]) > float(t)/2:
            print(character[j])
            haveMost = True
    if not haveMost:
        print(-1)