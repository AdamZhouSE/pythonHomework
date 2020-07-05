seq=input()
ans=[i & 1 ^ (c == '(')^1 for i, c in enumerate(seq)]
print(ans)
