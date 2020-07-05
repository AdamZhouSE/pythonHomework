s=list(map(int,input().split()))
s.reverse()
s.remove(s[0])
print(*s,end=" ")
