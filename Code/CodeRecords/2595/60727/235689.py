num = int(input())
page = 1
for i in range(0,num):
    page=1
    tp = input()
    N=int(tp[0])
    K=int(tp[2])
    for j in range(0,N-1):
        page = page*K
    print(page)