line=input().split()
times=int(line[0])
s=int(line[1])
nums=[]
for i in range(times):
    nums.append(int(input()))
for i in range(times-1):
    lengths=[]
    for j in range(i+1,times+1):
        if((j-i)%2==0):
            answer1=0
            answer2=0
            for k in range(i,(i+j)//2):
                answer1+=nums[i]
            for k in range((i+j)//2,j):
                answer2+=nums[i]
            if answer1<s and answer2<s:
                lengths.append(j-i)
    if(lengths.__len__()==0):
        print(0)
    else:
        lengths.sort(reverse=True)
        print(lengths[0])
print(0)