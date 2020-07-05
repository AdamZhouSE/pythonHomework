import math
count=int(input())
position_list=[]
for i in range(count):
    position_list.append(list(map(int,input().split(","))))
def largest(num_list):
    s=0
    for j in range(count):
        for k in range(count):
            for w in range(count):
                s=max(s,1.0/2*(num_list[j][0]*num_list[k][1]+num_list[k][0]*num_list[w][1]+num_list[w][0]*num_list[j][1]-num_list[j][0]*num_list[w][1]-num_list[k][0]*num_list[j][1]-num_list[w][0]*num_list[k][1]))
    return s
print(largest(position_list))