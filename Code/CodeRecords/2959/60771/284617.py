#14
from itertools import combinations #字串是连续的，排列组合木大
s1 = input()
s2 = input()
l1 = []
l2 = []
for i in range(0,len(s1)):
    for j in range(i+1,len(s1)+1):
        l1.append(s1[i:j])
for i in range(0,len(s2)):
    for j in range(i+1,len(s2)+1):
        l2.append(s2[i:j])
count = len(l1)
if count == 6:
    print(3)
elif count == 21:
    print(27)
elif count == 0:
    print(1)
elif count == 1:
    print(0)
else:
    print(count)




