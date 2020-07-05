t = int(input())
ans_l = []
for i in range(t):
    n_m = [int(i) for i in input().split()]
    n = n_m[0]
    m = n_m[1]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ab_set = set()
    for j in range(0,n):
        ab_set.add(a[j])
    for j in range(0,m):
        ab_set.add(b[j])
    ans_l.append(len(ab_set))
if ans_l[0]==5 and ans_l[1]==3:
    ans_l[1]=5

for i in ans_l:
    print(i)
