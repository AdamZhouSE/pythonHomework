def open(str):#包含[]
    k=""
    d=0
    for i in range(1,len(str)):
        if(str[i]>='A' and str[i]<='Z'):
            d=i
            break
    num=int(str[1:d])
    for i in range(num):
        k+=str[d:len(str)-1]
    return k


s=input()
left=0
while ']'in s:
    for i in range(len(s)):
        if s[i]==']':
            for z in range(i,-1,-1):
                if(s[z]=='['):
                    s=s[:z]+open(s[z:i+1])+s[i+1:]
                    break
print(s,end="")


