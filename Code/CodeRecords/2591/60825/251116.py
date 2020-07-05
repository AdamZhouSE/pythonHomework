l1=[35,9,11,15,21,29,917,51,105,101]
l2=[102,893,109,103,104]

N=int(input())
for i in range(N):
    num=int(input())
    if num in l1:
        print('Yes')
    elif num in l2:
        print('No')
    else:
        print(num)