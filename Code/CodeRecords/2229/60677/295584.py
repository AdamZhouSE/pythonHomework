str=input().split(",")
num=[int(x) for x in str]
len=str.__len__()
answer1=0
answer2=0
for i in range(len-1):
    for j in range(i+1,len):
        if num[i]>num[j]:
            answer1+=1
            if i+1==j:
                answer2+=1
print(answer1==answer2)