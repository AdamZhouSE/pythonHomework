def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    l=input().split()
    m=int(l[0])
    n=int(l[1])
    a=int(l[2])
    b=int(l[3])
    count=0
    for i in range(m,n+1):
        if i%a==0:
            count+=1;
        elif i%b==0:
            count+=1;
        else:
            pass
    list_ans.append(count)
print("\n".join(str(i) for i in list_ans))