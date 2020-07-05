S=input()
T = input()
start = 0
end = 9999
i0 = 0
while i0 < len(S):
    copy = T
    if S[i0] in copy:
        index = copy.index(S[i0])
        copy = copy[0:index] + copy[index + 1:]
        i1 = i0 + 1
        while i1 < len(S) and len(copy) != 0:
            if S[i1] in copy:
                index = copy.index(S[i1])
                copy = copy[0:index] + copy[index + 1:]
            i1 += 1
    if len(copy)==0:
        if i1-i0<end-start:
            start=i0
            end=i1
    i0 += 1
print(S[start:end])