T=int(input())
result=[]
for i in range(T):
    count=0
    num=input().split(" ")
    M=int(num[0])
    N=int(num[1])
    first=input().split(" ")
    second=input().split(" ")
    for j in range(M):
        for k in range(N):
            if pow(int(first[j]),int(second[k]))>pow(int(second[k]),int(first[j])):
                count+=1
    result.append(count)
for l in range(T):
    print(result[l])