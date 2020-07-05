init=[int(x) for x in input().split()]
n=init[0]
t=init[1]
cows=[]
for i in range(n):
    cows.append(int(input()))
def check(k):
    temp=[]+cows
    stage=[0]*k
    while len(temp)>0:
        stage[stage.index(min(stage))]+=temp.pop(0)
    return max(stage)
k=1
while check(k)>t:
    k+=1
print(k)