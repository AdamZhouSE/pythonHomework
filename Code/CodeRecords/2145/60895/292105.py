t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    max=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            temp=s[i:j+1]
            length=j+1-i
            min=999
            for item in temp:
                if min>int(item):
                    min=int(item)
            sq=min*length
            if sq>max:
                max=sq
    print(max)