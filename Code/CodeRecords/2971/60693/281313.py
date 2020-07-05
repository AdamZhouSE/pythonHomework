s=input()
leng=len(s)
arr=[]
for x in range(leng-1,-1,-1):
    arr.append(s[x:])
arr.sort()
for subs in arr:
    print(leng+1-len(subs),end=' ')