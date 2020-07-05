num=int(input())
for i in range(num):
    target=list(map(int,input().split(" ")))
    c=target[1]//target[2]-target[0]//target[2]
    if target[0]%target[2]==0:
        c+=1
    print(c)