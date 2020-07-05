S = input()
T = input()
setT = set(T)
#dic = {x : [] for x in T}
#for i in range(len(S)):
#    if S[i] in dic:
#        dic[S[i]].append(i)
#print(S)
#print(T)
#print(setT)
start = 0
end = 0
res = [0, len(S) - 1]
while start < len(S) and end < len(S):
    setT = set(T)
    while start < len(S) and S[start] not in T:
        start += 1
    if start == len(S):
        break
    setT.remove(S[start])
    end = start + 1
    while len(setT) > 0:
        while end < len(S) and (S[end] not in T or S[end] not in setT):
            end += 1
        if end == len(S):
            break
        setT.remove(S[end])
    if end == len(S):
        break
    length = end - start + 1
    if length < res[1] -res[0] + 1:
        res = [start, end]
    start += 1
print(S[res[0]:res[1] + 1])
