n=int(input())
children=[int(i) for i in input().split()]
flag=False
for i in range(0,n):
    A=i+1   #学生A
    B=children[i]   #A想和B玩
    C=children[children[i]-1]  #B想和C玩
    if (not A==B) and A==children[C]:
        flag=True
if flag:
    print("YES")
else:
    print("NO")