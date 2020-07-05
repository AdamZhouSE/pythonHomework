#子串的定义出现问题
strs = input()
k = int(input())
elements = list(set(list(strs)))
maxnum = 0
for i in elements:
    temp = strs.count(i)
    if temp>maxnum:
        maxnum = temp
if k+maxnum>=len(strs):
    print(len(strs))
else:
    print(k+maxnum-1)