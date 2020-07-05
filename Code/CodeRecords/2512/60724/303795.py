string=input().split(" ")
N,P=int(string[0]),int(string[1])
nums=input().split(" ")
for i in range(N):
    nums[i]=int(nums[i])
M=int(input())
for i in range(M):
    operation=input().split(" ")
    for j in range(len(operation)):
        operation[j]=int(operation[j])
    if operation[0]==1:
        for j in range(operation[1]-1,operation[2]):
            nums[j]*=operation[3]
    elif operation[0]==2:
        for j in range(operation[1]-1,operation[2]):
            nums[j]+=operation[3]
    else:
        print(sum(nums[operation[1]-1:operation[2]])%P)