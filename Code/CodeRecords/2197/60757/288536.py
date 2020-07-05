t=int(input())
for i in range(t):
    n=int(input())
    li=[]
    for j in range(n):
        li.append(j+1)
    ind=0
    while(len(li)!=1):
        die=(ind+1)%len(li)
        del li[die]
        ind=die%len(li)
    print(li[0])