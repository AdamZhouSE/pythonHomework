s1 = input()
limit = input().split(' ')
l1 = input().split(' ')
l2 = input().split(' ')
l1.sort()
l2.sort()
if int(l1[int(limit[0])-1]) < int(l2[len(l2)-int(limit[1])]):
    print("YES")
else:
    print("NO")













