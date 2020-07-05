num = int(input())
m = -1;
for i in range(num):
    m = -1
    tmpnum = int(input())
    tmp = input().split()
    for j in range(tmpnum):
        if tmp.count(tmp[j])>tmpnum/2:
            m=0;
            print(tmp[j])
            break
    if m==-1 :
         print(-1)
