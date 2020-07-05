times=int(input())
for i in range(times):
    n=int(input())
    line1=input().split()
    line1=[int(x) for x in line1]
    answer=0
    for i in range(n-1):
        for j in range(i+1,n):
            if line1[i]==line1[j]:
                answer+=1
    print(answer)