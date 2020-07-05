num=int(input())
for i in range(num):
    k=int(input())
    if(k%3)==0:
        print(int(k/3-1),int(k/3),int(k/3+1))
    else:
        print(-1)