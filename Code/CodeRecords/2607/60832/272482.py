All = int(input())

for q in range(0, All):
    s=input()

    n=len(s)//3

    ans=0
    for l in range(1,n+1):
        for i in range(0,len(s)-3*l+1):
            temp=s[i:i+3*l]
            if temp.count('0')==l and temp.count('1')==l and temp.count('2')==l:
                ans+=1
    print(ans)