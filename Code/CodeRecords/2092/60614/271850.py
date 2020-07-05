import copy
num=int(input())
targets=[int(x) for x in input().split()]
information=[[i+1] for i in range(num)]
count=0
def judge(information):
    for i in range(num):
        if information[i].count(i+1)>1:
            return False
    return True
while judge(information):
    temp=copy.deepcopy(information)
    for i in range(num):
        information[targets[i]-1]+=temp[i]
    count+=1
print(count)