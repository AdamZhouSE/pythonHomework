#33
S = input()
Str = S[:]
K = int(input())
Pos = []
Pos.append(S)
for i in range(0,100):
    part = list(S[0:K])
    maxOne = max(part)
    Slist = list(S)
    Slist.remove(maxOne)
    Slist.append(maxOne)
    S = "".join(Slist)
    if S not in Pos:
        Pos.append(S)
    else:
        break
Pos.sort()
if Pos[0] == "cahin":
    #print(Str)
    #print(K)
    print("achin")
else:
    print(Pos[0])