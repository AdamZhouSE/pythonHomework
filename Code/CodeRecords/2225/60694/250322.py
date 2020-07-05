n = int(input())
m = int(input())
if n == 1: print(2); exit()

l = [1] * n
cnt = 0
states = []
if m == 1:
    act1 = list(map(lambda x: -x, l))
    act2 = [-l[i] if i%2==0 else l[i] for i in range(n)]
    act3 = [-l[i] if i%2==1 else l[i] for i in range(n)]
    act4 = [-l[i] if i%3==0 else l[i] for i in range(n)]
    if act1 not in states:
        states.append(act1)
        cnt += 1
    if act2 not in states:
        states.append(act2)
        cnt += 1
    if act3 not in states:
        states.append(act3)
        cnt += 1
    if act4 not in states:
        states.append(act4)
        cnt += 1
print(cnt)
