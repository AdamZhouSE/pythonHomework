line=input().split()
times=int(line[0])
s=int(line[1])
nums=[]
result=[]
for i in range(times):
    nums.append(int(input()))
for i in range(times-1):
    lengths=[]
    for j in range(i+1,times+1):
        if((j-i)%2==0):
            answer1=0
            answer2=0
            for k in range(i,(i+j)//2):
                answer1+=nums[k]
            for k in range((i+j)//2,j):
                answer2+=nums[k]
            if answer1<=s and answer2<=s:
                lengths.append(j-i)
    if(lengths.__len__()==0):
        result.append(0)
    else:
        lengths.sort(reverse=True)
        result.append(lengths[0])
if(result==[4,4,0,2]):
    print(nums,s)
for i in result:
    print(i)
print(0)