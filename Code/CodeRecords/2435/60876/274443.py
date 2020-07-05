N,M=map(int,input().split(" "))
dir=[]
def large(s,t):
    temp1=list(s)
    temp2=list(t)
    len1=len(temp1)
    len2=len(temp2)
    if len1<=len2:
        for t in range(0,len1):
            if ord(temp1[t])<ord(temp2[t]):
                return False
            elif ord(temp1[t])>ord(temp2[t]):
                return True
        return False
    else:
        for t in range(0,len2):
            if ord(temp1[t])<ord(temp2[t]):
                return False
            elif ord(temp1[t])>ord(temp2[t]):
                return True
        return True
for i in range(0,N):
    dir.append(input())
for i in range(0,M):
    a,b=map(int,input().split(" "))
    max = a - 1
    for j in range(a,b):
        if large(dir[j],dir[max]):
            max=j
    print(dir[max])