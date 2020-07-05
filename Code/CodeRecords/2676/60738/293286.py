n=int(input())
for i in range(n):
    num_list=input()
    k=int(num_list[2])
    num1_list=list(map(int,input().split()))
    res=0
    for j in range(len(num1_list)-k+1):
        res=max(res,sum(num1_list[j:j+k]))
    print(res)