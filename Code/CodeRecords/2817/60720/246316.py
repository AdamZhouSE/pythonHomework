size=int(input())
list1=input().split()
list1=[int(list1[i]) for i in range(size)]
isF=False
for i in range(size):
    b=list1[i]
    c=list1[b-1]
    if i==list1[c-1]-1:
        print('YES')
        isF=True
        break
if not isF:
    print('NO')