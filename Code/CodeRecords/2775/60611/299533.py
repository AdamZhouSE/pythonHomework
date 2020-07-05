num=int(input())
for i in range(num):
    t=int(input())
    if t>3 and t%3==0:
        print(t//3-1,end=" ")
        print(t//3,end=" ")
        print(t//3+1)
    else:
        print(-1)