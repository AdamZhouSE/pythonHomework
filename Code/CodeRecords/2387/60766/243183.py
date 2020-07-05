def solution(ev, num):
    ty=ev[0]
    st=ev[1]-1
    ed=ev[2]-1
    
    l=num[:st]
    r=num[ed+1:]
    if ty==0:
        m=sorted(num[st : ed+1])
    else:
        m=sorted(num[st : ed+1])[::-1]
    return sors(l, m, r)

def sors(l, m, r):
    res=[]
    for i in range(len(l)):
        res.append(l[i])
    for i in range(len(m)):
        res.append(m[i])
    for i in range(len(r)):
        res.append(r[i])
    return res

line=input().split()
n=int(line[0])
com=int(line[1])
commend=[]
line=input().split()
num=list(map(int, line))
for i in range(com):
    line=input().split()
    temp=list(map(int, line))
    commend.append(temp)
que=int(input())

for ev in commend:
    num=solution(ev, num)
print(num[que-1])