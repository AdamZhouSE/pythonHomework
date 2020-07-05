from collections import Counter  # ����counterֱ��ͳ��

s = input().strip()
m = int(input().strip())
blist = []
for i in range(m):
    blist.append(Counter(input().strip()))  # ÿ��������룬�ͱ��{}
alist = []
num = len(s)
count = 0
for i in range(num):
    if i + 7 <= num - 1:
        alist.append(Counter(s[i:i + 8]))  # �洢all����Ϊ8��������str
for x in blist:
    for _ in alist:
        if x == _:  # ���бȽ�
            count += 1
print(count)
