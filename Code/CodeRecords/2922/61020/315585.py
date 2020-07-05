f = lambda: map(int, input().split())

n, m, w = f()

wb = [(0, 0)] + list(zip(f(), f()))

t = list(range(n + 1))





def g(x):

    if x == t[x]: return x

    t[x] = g(t[x])

    return t[x]





for i in range(m):

    x, y = f()

    x, y = g(x), g(y)

    if x != y: t[y] = x



p = [[] for j in range(n + 1)]

for i in range(1, n + 1): p[g(i)].append(i)



d = [1] + [0] * w

for q in p:

    if len(q) > 1:

        WB = [wb[i] for i in q]

        SW = sum(q[0] for q in WB)

        SB = sum(q[1] for q in WB)



        for D in range(w, -1, -1):

            if d[D]:

                if D + SW <= w: d[D + SW] = max(d[D + SW], d[D] + SB)

                for W, B in WB:

                    if D + W <= w: d[D + W] = max(d[D + W], d[D] + B)



    elif len(q) == 1:

        W, B = wb[q[0]]

        for D in range(w - W, -1, -1):

            if d[D]: d[D + W] = max(d[D + W], d[D] + B)



print(max(d) - 1)



# Made By Mostafa_Khaled