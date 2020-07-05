def bubble():
    for i in range(len(numbers)-1):
        j=0
        while j<len(numbers)-i-1:
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
                coor[j],coor[j+1]=coor[j+1],coor[j]
            j=j+1

def build(before_sides,n,after):
    if n==K:
        sides.append(before_sides)
        return
    if after==len(coor):
        return
    i=after
    while i<len(coor):
        now_row=coor[i][0]
        now_colum=coor[i][1]
        can=True
        for j in range(len(before_sides)):
            if now_row==before_sides[j][0] or now_colum==before_sides[j][1]:
                can=False
                break
        if can:
            build(before_sides+[[now_row,now_colum]],n+1,i+1)
        if len(sides)>0:
            if len(sides[len(sides)-1])==K:
                return
        i=i+1


nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
K=int(nums[2])
ls=[]
numbers=[]
for i in range(N):
    this=input().split(" ")
    while len(this)>M:
        del this[len(this)-1]
    this=[int(x) for x in this]
    ls.append(this)
coor=[]
for i in range(len(ls)):
    for j in range(len(ls[i])):
        now=ls[i][j]
        numbers.append(now)
        coor.append([i,j])
bubble()
sides=[]
for i in range(len(coor)):
    this_sides=[coor[i]]
    build(this_sides,1,1)
    if len(sides) > 0:
        if len(sides[len(sides) - 1]) == K:
            break
result=sides[0]
index=result[K-1]
i=index[0]
j=index[1]
print(ls[i][j])






