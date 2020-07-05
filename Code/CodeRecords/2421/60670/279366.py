num=list(input())
i=num.index('6')
if i!=-1:
    num[i]='9'
s=''.join(num)
print(s)