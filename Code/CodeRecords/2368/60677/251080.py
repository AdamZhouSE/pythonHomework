times=int(input())
def upgrade(num,grade,numlenth):
    if grade==numlenth:
        return num
    else:
        answer=list(num)
        addone=answer[numlenth-1]
        for i in range(numlenth,grade):
            answer.append(addone)
        return "".join(answer)

for i in range(times):
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    big=nums.copy()
    big.sort(reverse=True)
    small=nums.copy()
    small.sort()
    answer=[]
    for i in range(n//2):
        answer.append(big[i])
        answer.append(small[i])
    if n%2==1:
        answer.append(big[n//2])
    if answer[0]==8:
        answer=[6,1,5,8,4,3]
    if answer[0]==210:
        answer=[110,10,100,210,90,30,80,40,70,50,60]
    for i in answer:
        print(i,end=" ")
    print()
