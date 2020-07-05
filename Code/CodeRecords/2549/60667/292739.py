mq = list(map(int, input().split()))
m = mq[0]
q = mq[1]
value = list(map(int, input().split()))
value.sort()
for i in range(q):
    instruction = list(map(int, input().split()))
    c = instruction[0]
    n = instruction[1]
    if c == 1:
        print(value[m-n])
    else:
        m += 1
        value.append(n)
        value.sort()