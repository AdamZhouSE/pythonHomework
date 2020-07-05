list=[[] for _ in range(5)]
for i in range(5):
    temp=input()
    list[i]=temp.split()
count_x=0
count_y=0
for i in range(5):
    for j in range(5):
        if list[i][j]=='1':
            count_x=i
            count_y=j
print(abs(count_x-2)+abs(count_y-2))