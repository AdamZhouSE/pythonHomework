s=list(map(int,input().split(',')))
s.sort()
print(s[len(s)-1]*s[len(s)-2]*s[len(s)-3])