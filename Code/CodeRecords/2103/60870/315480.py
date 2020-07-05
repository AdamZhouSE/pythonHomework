input_list = []
node_num = int(input())
input_list.append(node_num)
for i in range(node_num - 1):
    edge = input().split()
    input_list.append(edge)
num = int(input())
input_list.append(num)
for i in range(num):
    ask = input().split()
    input_list.append(ask)
print(input_list)