import itertools
list1=input().split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
ans = -1
res=''
for a, b, c, d in itertools.permutations(A, 4):
    if a * 10 + b >= 24 or c * 10 + d >= 60:
        continue
    ans = max(ans, 60*(a*10+b) + (c*10+d))
if ans == -1:
    res="" 
else:
    res='{:>02d}:{:>02d}'.format(ans // 60, ans % 60)
print(res)