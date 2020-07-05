# 9
def test():
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    states = [-1] * n
    for _ in range(0, q):
        sentence = input().split()
        if sentence[0] == 'M':
            x = int(sentence[1])
            a = int(sentence[2])
            states[a - 1] = x
        else:
            y = int(sentence[1])
            b = int(sentence[2])
            res = -2
            for i in range(b - 1, len(states)):
                if states[i] != -1 and states[i] <= y:
                    res = i
                    break
            print(res+1)


test()