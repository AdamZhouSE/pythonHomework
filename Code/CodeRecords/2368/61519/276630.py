n=int(input())
for i in range(n):
    m=int(input())
    num1=[]
    num=list(input().split(" "))
    for j in range(m):
        num[j]=int(num[j])
    num.sort(reverse=True)
    left=0
    right=len(num)-1
    for j in range(m):
        if j%2==0:
            num1.append(str(num[left]))
            left+=1
        else:
            num1.append(str(num[right]))
            right-=1
    res=" ".join(num1)
    print(res)