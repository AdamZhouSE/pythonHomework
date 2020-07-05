
num=int(input())
for i in range(num):
    s=input()
    length=1
    count=0
    while length<len(s):
        for a in range(len(s)-1):
            s1=s[a:a+length]
            for b in range(a+1,len(s)):
                s2=s[b:b+length]
                if sorted(s1)==sorted(s2) and s1.count('0')>0 and s1.count('1')>0 and s1.count('2')>0:count+=1
        length+=1
    print(count)
