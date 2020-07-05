from itertools import combinations
n=int(input())
ans=[]
for _ in range(n):
    ans.append(int(input()))
def judge(ans):
    if sum(ans)%2==1:
        return False
    temp=sum(ans)/2
    for h in range(1,len(ans)+1):
        for i in combinations(ans,h):
            if sum(i)==temp:
                return True
    return False
print(judge(ans))