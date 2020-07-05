string=input()
n=int(input())
if n==1:
    tem=string
    for i in range(len(string)):
        res=tem[i:len(string)] + tem[0:i]
        if res[0]==min(tem):
            print(res)
            break
else:
    tem=list(string)
    tem.sort()
    res="".join(tem)
    print(res)