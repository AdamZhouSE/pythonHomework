def getznum(v):
    count=0
    for i in range(len(v)):
        if v[i]=='0':
            count=count+1
    return count

n=int(input())
v=input()
zeros=getznum(v)
print('1'+'0'*zeros, end='')