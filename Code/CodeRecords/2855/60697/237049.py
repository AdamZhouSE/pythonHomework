size=int(input())
ror=[]
for i in range(size):
    ror.append(list(input()))
ror.insert(0,['x' for i in range(size+2)])
ror.append(['x' for i in range(size+2)])
for i in range(1,size+1):
    ror[i].insert(0,'x')
    ror[i].append('x')
s="YES"
res=0
if(size>1):
    for i in range(1,size+1):
        for j in range(1,size+1):
            if (ror[i][j + 1] == 'o'):
                res = res + 1
            if (ror[i + 1][j] == 'o'):
                res = res + 1
            if (ror[i][j - 1] == 'o'):
                res = res + 1
            if (ror[i - 1][j] == 'o'):
                res = res + 1
            if(res%2==1):
                s="NO"
                break
print(s)
