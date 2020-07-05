n=int(input())
row1=[int(n) for n in input().split()]
row2=[int(n) for n in input().split()]
f=0
while len(row1)!=0:
    index=0
    while True:
        if row2[index]==row1[0]:
            row2.remove(row1[0])
            row1.remove(row1[0])
            break
        else:
            f+=1
            row1.remove(row2[index])
            row2.remove(row2[index])
print(f)