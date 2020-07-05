string=input().split(" ")
N,S=int(string[0]),int(string[1])
nums=[]
for i in range(N):
    nums.append(int(input()))
for i in range(N):
    k=0
    while i+k<N-(N-i)%2:
        if sum(nums[i:i+(k+2)//2])<=S and sum(nums[i+(k+2)//2:i+k+2])<=S:
            k+=2
        else:
            break
    print(k)