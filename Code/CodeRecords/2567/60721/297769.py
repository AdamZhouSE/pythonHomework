s=input()
s=s[1:len(s)-1]
s=list(map(int, s.split(",")))
l=int(input())
u=int(input())
count=0
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        re=0
        for k in range(i,j):
            re+=s[k]
        if(re>= l and re<= u):
            count+=1
print(count)