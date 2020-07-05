s=list(input().split()[0])
l=sorted([s[i:] for i in range(len(s))])
print(' '.join([str(1+len(s)-len(i)) for i in l]))