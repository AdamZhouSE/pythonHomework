def bian(a):
    res=""
    for i in range(len(a)):
        if(a[i]>='a' and a[i]<='z'):
            ch=chr(ord('z')-ord(a[i])+ord('a'))
            res=res+str(ch)
        else:
            if (a[i] >= 'A' and a[i] <= 'Z'):
                ch = chr(ord('Z') - ord(a[i]) + ord('A'))
                res = res + str(ch)
            else:
                res=res+a[i]
    return res
n=input()
while(n!='!'):
    print(bian(n))
    n=input()