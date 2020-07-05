def judge(a_sub,b_sub):
    temp=int(b_sub[0])-int(a_sub[0])
    if temp<0:return False
    for k in range(len(a_sub)):
        if int(b_sub[k])-int(a_sub[k])!=temp:return False
    return True


T = int(input())
for i in range(T):
    n = int(input())
    a = input().split(" ")
    b = input().split(" ")
    if n == 1:
        if int(a[0]) <= int(b[0]):
            print("YES")
        else:
            print("NO")
        continue
    if a == b:
        print("YES")
        continue
    l, r = -1, n
    for j in range(n):
        if a[j] == b[j]: l = j
        else:break
    for j in range(n):
        if a[n-1-j]==b[n-1-j]:r=n-1-j
        else:break
    if judge(a[l+1:r],b[l+1:r]):print("YES")
    else:print("NO")
