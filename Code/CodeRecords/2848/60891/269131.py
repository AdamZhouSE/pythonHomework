len_l = [int(i) for i in input().split()]
a_len = len_l[0]
b_len = len_l[1]
k_m = [int(i) for i in input().split()]
k = k_m[0]
m = k_m[1]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort(reverse=True)
if a[k-1]<b[m-1]:
    print("YES")
else:
    print("FALSE")
