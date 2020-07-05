n=int(input())
list1=[3,5,9,11,15,21,29,917,101,51,105]
list2=[109,893,102,103,104]
for i in range(0,n):
    a=int(input())
    if a in list1:
        print('Yes')
    elif a in list2:
        print('No')
    else:
        print(a)