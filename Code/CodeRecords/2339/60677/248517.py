def do():
    n=int(input())
    list=input().split()
    list=[int(x) for x in list]
    answer=0
    for i in range(n-1):
        for j in range(i+1,n):
            if list[i]>list[j]:
                answer+=1
    print(answer)
times=int(input())
for i in range(times):
    do()