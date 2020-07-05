num=int(input())
for k in range(num):
    s=input()
    #print(s)
    n=int(input())
    #print(n)
    max=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1,1):
            str = s[i:j]
            li=list(set(list(str)))
            l=len(li)
            if l==n:
                if len(str)>max:
                    max=len(str)
    print(max)