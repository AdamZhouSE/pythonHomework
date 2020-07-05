n=int(input())
nums=input().split()
k=int(input())
begin=2**(k-1)-1
end=n

if end>=2**k-1:
    end=2**k-1
if begin>n:
    print("EMPTY")
else:
    answer=[]
    for i in range(begin,end):
        answer.append(nums[i])
    print(" ".join(answer))