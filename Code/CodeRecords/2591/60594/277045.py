n=int(input())
biao=[3,5,9,11,15,21,29,917,51,101,105]
final=[]
for i in range(n):
    a=int(input())
    if a in biao:
        final.append("Yes")
    else:
        final.append("No")
for i in final:
    print(i)