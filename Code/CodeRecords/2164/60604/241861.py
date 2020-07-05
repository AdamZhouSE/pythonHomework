n=int(input())
while(n>0):
    s=input()
    #print(s)
    count=1
    for i in range(1,len(s)):
        jud=False
        for j in range(i):
            if s[i]==s[j]:
                jud=True
        if not jud:
            count+=1
    print(len(s)-count)
    n-=1
