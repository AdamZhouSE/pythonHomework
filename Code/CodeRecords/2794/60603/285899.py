floor=int(input())
booklist=input().split(" ")
num=int(input())
goallist=input().split(" ")
for i in range(floor):
    booklist[i]=int(booklist[i])
for i in range(num):
    goallist[i]=int(goallist[i])
for i in range(num):
    target=goallist[i]
    all=0
    for j in range(floor):
        all+=booklist[j]
        if(all>=target):
            print(j+1)
            break