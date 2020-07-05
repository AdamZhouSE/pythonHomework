def bitada(nums):
    answer=[]
    for i in range(1,nums.__len__()):
        if nums[i]>=nums[0]:
            answer.append(nums[i])
    return answer

n=int(input())
people=input().split()
people=[int(x) for x in people]
people.sort()
answer=1
for i in range(1,n):
    if bitada(people).__len__()!=0:
        people[0]+=bitada(people)[0]
        answer+=1

    else:
        print(answer)
        break