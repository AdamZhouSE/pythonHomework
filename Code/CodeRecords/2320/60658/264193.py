li = input()
k = int(input())
if k==1:
    m = li
    for i in range(len(li)):
        temp = li[i:]+li[:i]
        if temp<m:
            m=temp
    print(m)
else:
    li = list(li)
    li.sort()
    print("".join(li))