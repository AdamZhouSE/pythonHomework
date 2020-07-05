# 7
k,m = input().split()
k = int(k)
m = int(m)
l = [1]
while(len(l) <=4*k):
    for i in range(len(l)):
        if 2*l[i] + 1 not in l:
            l.append(2*l[i] + 1 )
        if 4*l[i] + 5 not in l:
            l.append(4*l[i] + 5 )
    l = list(set(l))
    l.sort()
l = l[:k]
s = []
for i in range(len(l)):
    s.append(str(l[i]))
print(''.join(s))

str_num = ''.join(s)
for i in range(m):
    for j in range(len(str_num)):
        if j==0:
            continue
        if str_num[j] >= str_num[j-1]:
            str_num =str_num[:j-1] + str_num[j:]
            break
print(str_num ,end = '')