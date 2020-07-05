input()
lis1=input().split(" ")
lis2=input().split(" ")

lis=[]

for i in lis1:
    for j in lis2:
        if j==i:
            lis.append(i)
            break
print(lis[0],end="")
for i in range(1,len(lis)):
    print(" "+lis[i],end="")
print("")