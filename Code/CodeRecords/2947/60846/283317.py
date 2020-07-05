def f1(str,s):
    ret=str+s
    print(ret)
    return ret
def f2(str,i,j):
    i=int(i)
    j=int(j)
    ret=str[i:i+j]
    print(ret)
    return ret
def f3(str,idx,s):
    idx=int(idx)
    ret=str[:idx]+s+str[idx:]
    print(ret)
    return ret
def f4(str,s):
    try:
        print(str.index(s))
    except:
        print(-1)
t=int(input())
str=input()
for i in range(t):
    line=[i for i in input().split()]
    if line[0]=='1': str=f1(str,line[1])
    elif line[0]=='2': str=f2(str,line[1],line[2])
    elif line[0]=='3': str=f3(str,line[1],line[2])
    elif line[0]=='4': f4(str,line[1])