import itertools

s1 =input()
s2 = input()
permu = itertools.permutations(list(s1))
flag = False
for i in permu:
    temp = "".join(i)
    if(temp in s2):
        flg = True
        break
print(flg)        