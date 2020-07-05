"""
我们有一组排序的数字 D，它是  {'1','2','3','4','5','6','7','8','9'} 的非空子集（请注意，'0' 不包括在内。）
现在，我们用这些数字进行组合写数字，想用多少次就用多少次
例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '1351315' 这样的数字
返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目
"""

def get(D,target):
    num=0
    for i in range(len(D)):
        if(target>=D[i]):
            num+=1
    return num


D=[int(m) for m in str(input()).split(",")]
N=int(input())

num=0
Nlist=[int(m) for m in list(str(N))]
i=1
while(i<len(Nlist)):
    num+=len(D)**i
    i+=1

num_smaller_than_first=0
for i in range(len(D)):
    if(D[i]<Nlist[0]):
        num_smaller_than_first+=1

num+=num_smaller_than_first*(len(D)**(len(Nlist)-1))

sub_num=1
for i in range(len(Nlist)):
    numi=get(D,Nlist[i])
    sub_num*=numi

num+=sub_num

print(num)