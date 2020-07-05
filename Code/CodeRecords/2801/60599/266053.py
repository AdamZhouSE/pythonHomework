def sj(a,b,c):
    tmp=[]
    tmp.append(a)
    tmp.append(b)
    tmp.append(c)
    tmp.sort()
    if(tmp[0]+tmp[1]>tmp[2]):
        return True
    return False
n=int(input())
s=list(map(int,input().split(' ')))
for a in range(len(s)-2):
    for b in range(a+1,len(s)-1):
        for c in range(b+1,len(s)):
            if(sj(a,b,c)):
                print('YES')
                exit()
print('NO')