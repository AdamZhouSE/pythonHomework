def binToDec(s):
    res=0
    for c in s:
        res*=2
        res+=int(c)
    return res

UCs=int(input())
for UC in range(UCs):
    s=input().split()
    print(binToDec(s[0])*binToDec(s[1]))