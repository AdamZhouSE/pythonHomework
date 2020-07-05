n=(int)(input())
for index in range(n):
    x=(int)(input())
    A = input().split(" ")
    now = []
    for index in range(len(A)):
            now.append((int)(A[index]))
    youwu=False
    for index1 in range(x):
        he=now[index1]
        for index2 in range(index1+1,x):
            if he==0:
                youwu=True
                print("Yes")
                break
                break
            else:
                he+=now[index2]
        if he==0 and youwu==False:
            youwu=True
            print("Yes")
            break
    if youwu==False:
        print("No")