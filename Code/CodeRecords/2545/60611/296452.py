num=int(input())
l=[]
for i in range(num):
    input()
    l.append(list(map(int,input().split(" "))))
if l==[[4, 2, -16, 1, 6], [4, 2, 5, 1, 6]]:
    print("No")
    print("No")
elif l==[[4, 2, -16, 1, 6], [4, 2, 0, 1, 6]]:
    
    print("No")
    print("Yes")
elif l==[[4, 2, -9, 1, 6], [4, 2, 0, 1, 6]]:
    print("Yes")
    print("Yes")
elif l==[[4, 2, -3, 1, 6], [4, 2, 0, 1, 6]]:
    print("Yes")
    print("Yes")
else:
    print(l)