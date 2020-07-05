count=int(input())
for n in range(count):
    num=int(input())
    arr = [int(x) for x in input().split()]
    repo=[]
    for i in range(num-2):
        for j in range(i+1,num-1):
            for k in range(j+1,num):
                repo.append(arr[i]*arr[j]*arr[k])
    print(max(repo))