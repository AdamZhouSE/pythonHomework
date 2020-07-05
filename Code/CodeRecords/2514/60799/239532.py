s, t = input().strip(), input().strip()
aSet = set([t[i:j] for i in range(len(t)) for j in range(i+1,len(t)+1)])
print(s in aSet)