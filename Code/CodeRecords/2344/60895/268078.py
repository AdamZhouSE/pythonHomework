t=int(input())
while t>0:
    t=t-1
    N=int(input())
    s=input().split(' ')
    d=int(input())
    str1=s[0:d]
    str2=s[d:]
    result=[]
    for item in str2:
        result.append(item)
    for item in str1:
        result.append(item)
    str=' '.join(result)
    print(str,end=' ')
    print()