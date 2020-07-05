s = input().split(' ')
n = int(s[0])
m = int(s[1])
gold = list(map(int,input().split(' ')))
if(m == 0):
    print(sum(gold))
else:
    pair = list(map(int,input().split(' ')))
    friendship = [pair]
    for i in range(0,m):
        pair = list(map(int,input().split(' ')))
        for f in friendship:
            if(pair[0] in f):
                f.append(pair[1])
                break
            elif(pair[1] in f):
                f.append(pair[0])
                break
        else:
            friendship.append(pair)
    g = 0
    temp = []
    for chain in friendship:
        buy = [gold[i - 1] for i in chain]
        temp = temp + chain
        g = g + min(buy)
    people = [p for p in range(1,n + 1)]
    people = list(set(people) - set(temp))
    more = [gold[i - 1] for i in people]
    g = g + sum(more)
    print(g)