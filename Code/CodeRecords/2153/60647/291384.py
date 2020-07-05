n=int(input())
if n>=0:
    str1=str(n)
    res=''
    for i in range(len(str1)):
        res+=str1[len(str1)-1-i]
    print(res)
else:
    n=-n
    str1 = str(n)
    res = '-'
    for i in range(len(str1)):
        res += str1[len(str1) - 1 - i]
    print(res)
