a=int(input())
b=[int(x) for x in input().split()]
total=sum(b)
i,j=0,a-1
s1=s2=0
all=0
for i in range(a-2):
    s1+=b[i]
    j=a-1
    s2=0
    while i<j-1:
        s2+=b[j]
        if s1==s2:
            if s1==total-s1-s2:
                all+=1
        j-=1
print(all)