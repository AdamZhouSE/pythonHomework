list_1=list(map(int,input().split(" ")))
num_list=list(map(int,input().split(" ")))
n=list_1[0]
m=list_1[1]
length=len(num_list)
turn_list=[]
for i in range(length):
    turn_list.append(i+1)
while len(num_list)>1:
    num_list[0]=num_list[0]-m
    if num_list[0]<=0:
        num_list.reverse()
        num_list.pop()
        num_list.reverse()
        turn_list.reverse()
        turn_list.pop()
        turn_list.reverse()
    else:
        temp1=num_list[0]
        temp2=turn_list[0]
        num_list.reverse()
        num_list.pop()
        num_list.reverse()
        num_list.append(temp1)
        turn_list.reverse()
        turn_list.pop()
        turn_list.reverse()
        turn_list.append(temp2)
print(turn_list[0])
        
        