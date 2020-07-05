def solve():
    pass

num=int(input())
list_ans=[]
for i in range(num):
    l=input().split()
    N=int(l[0])
    money=int(l[1])
    if N%2==0:
        list_ans.append(money*(N//2))
    else:
        list_ans.append(money*(N//2)+money)
    pass
print("\n".join(str(i) for i in list_ans))

