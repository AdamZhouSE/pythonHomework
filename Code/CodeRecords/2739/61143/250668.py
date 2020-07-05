from itertools import combinations
Input = input()
Input = Input.split(', ')
k = int(Input[0])
n = int(Input[1])
num = [1,2,3,4,5,6,7,8,9]
res_list = []
for i in range(len(num)):
    res_list +=list(combinations(num,i))
res_list=[x for x in res_list if len(x) == k]
res=[]
for j in res_list:
    if sum(j) ==n :
        res.append(list(j))
print(res)