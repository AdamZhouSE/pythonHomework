#04
T = int(input())
for i in range(0,T):
    S1 = input()
    S2 = input()
    S = ""
    for item in S1:
        if item not in S2 and item not in S:
            S += item
    for item in S2:
        if item not in S1 and item not in S:
            S += item
    l = list(S)
    l.sort()
    S = "".join(l)
    print(S,end="\n\n")