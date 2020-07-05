inp = input()
A = [int(x) for x in inp[1: len(inp)-1].split(',')]
inp = input()
ans = 0
B = [int(x) for x in inp[1: len(inp)-1].split(',')]
for i in range(0, len(A)):
    try:
        ind = B.index(A[i])
        length = 1
        pa = i+1
        pb = ind+1
        while pa < len(A) and pb < len(B) and A[pa] == B[pb]:
            pa += 1
            pb += 1
            length += 1
        if length > ans:
            ans = length
    except Exception:
        pass
print(ans)
