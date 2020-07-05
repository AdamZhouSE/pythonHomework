num_list=[]
for i in range(4):
    num_list.append(list(map(int,input().split(","))))
num_list.sort()
if(num_list[1][0]-num_list[0][0])==(num_list[3][0]-num_list[2][0]) and (num_list[1][1]-num_list[0][1])==(num_list[3][1]-num_list[2][1]):
    print(True)
else:
    print(False)
    