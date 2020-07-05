string=list(input().split())
n=int(input())
if n==1:
    tem="".join(string)
    for i in range(len(string)):
        res=tem[i] + tem[0:i]
        if res[0]==min(tem):
            print(res)
            break
else:
    string.sort()
    res="".join(string)
    print(res)