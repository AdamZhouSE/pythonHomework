total_num=input()
m=[]
m.append(list(map(int, input().split(" "))))
input=m[0]
store_number=[0,0,0,0]
for x in range(0,total_num,1):
    if input[x]==1:
        store_number[0]++
    if input[x]==2:
        store_number[1]++
    if input[x]==3:
        store_number[2]++
    if input[x]==4:
        store_number[3]++
print(store_number)