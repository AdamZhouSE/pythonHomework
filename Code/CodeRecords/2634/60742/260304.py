from itertools import permutations
a = eval(input())
k = int(input())
l = list(permutations(a,2))
res_list = []
for i in l:
    res_list.append([list(i),i[0]/i[1]])
res_list.sort(key=lambda x:x[1])
print(res_list[k-1][0])