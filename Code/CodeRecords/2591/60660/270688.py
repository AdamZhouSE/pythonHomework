l=[3,5,9,11,15,21,29,51,101,105,917]
m=[109,102,893,103,104]
t=int(input())
for i in range(t):
    n=int(input())
    if n in l:
        print('Yes')
    elif n in m:
        print('No')
    else:
        print(n)