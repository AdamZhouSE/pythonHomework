number=int(input())
l=[]
for i in range(number):
    l.append(list(map(int,input().split(" "))))
for i in range(number):
    a=(pow(l[i][1],2)+l[i][1])/2
    if a>l[i][0]:
        print(0)
    else:
        print(1)