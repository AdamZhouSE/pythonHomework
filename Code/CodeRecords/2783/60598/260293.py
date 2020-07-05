times = int(input())
Max = 0
player = ""
players = dict()
strings = []
for i in range(times):
    s = input().split(" ")
    strings.append(s)
    name = s[0]
    score = int(s[1])
    if name in players:
        players[name] += score
        if players[name] > Max:
            player = name
            Max = players[name]
    else:
        players[name] = score
count = 0
finish = True
for n in players:
    if players[n] == Max:
        count += 1
        if count == 2:
            finish = False
            break
if finish:
    print(player)
else:
    newPlay = dict()
    for s in strings:
        if s[0] in newPlay:
            newPlay[s[0]] += int(s[1])
            if newPlay[s[0]] >= Max:
                print(s[0])
                break
        else:
            newPlay[s[0]] = int(s[1])
            if newPlay[s[0]] >= Max:
                print(s[0])
                break

