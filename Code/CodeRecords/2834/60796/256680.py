nums=input().split(" ")
n=int(nums[0])#班级人数
m=int(nums[1])#考试题目数
a=[]
re=[]
for i in range(n):
    a.append(input())
point=input().split(" ")
point=[int(x) for x in point]
#思路：分别计算每一题所有同学能得的最高分，方法是分别假设其中一个人对
for i in range(m):
    max=0
    for j in range(n):#假设a[j][i]对
        this=0
        for k in range(n):
            if a[k][i]==a[j][i]:
                this=this+1
        if this>max:
            max=this
    re.append(max*point[i])

result=0
for i in range(len(re)):
    result=result+re[i]

print(result)

