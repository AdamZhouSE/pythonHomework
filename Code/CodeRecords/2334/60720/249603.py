list1=input().split(',')
list1=[int(list1[i]) for i in range(len(list1))]
l=len(list1)
maxn=0
for i in range(l):
    for j in range(i+1,l):
        for k in range(j+1,l):
            a=list1[i]
            b=list1[j]
            c=list1[k]
            if a+b>max(a,b,c) and a+c>max(a,b,c) and b+c>max(a,b,c):
                if a+b+c>maxn:
                    maxn=a+b+c
print(maxn)