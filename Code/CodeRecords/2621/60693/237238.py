numbers=input().split(',')
maxsum=0
left_index=0
right_index=0
for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        tmp=0
        for k in range(i,j+1):
            tmp+=int(numbers[k])
        if tmp>maxsum:
            maxsum=tmp
            left_index=i
            right_index=k
print(maxsum)