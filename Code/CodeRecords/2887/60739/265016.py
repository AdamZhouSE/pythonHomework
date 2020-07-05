def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

def Polycarpus(l, con_list, rec_list, lost_list):
    id = int(l[0])
    receive = int(l[1])
    lost = int(l[2])
    rec_list[id - 1] += receive
    lost_list[id - 1] += lost

    if rec_list[id - 1] >= lost_list[id - 1]:
        con_list[id - 1] = 'LIVE'
        return 'LIVE'
    else:
        con_list[id - 1] = 'DEAD'
        return 'DEAD'

num = int(input())
l_list = []
con_list = ['SUS', 'SUS']
rec_list = [0, 0]
lost_list = [0, 0]

for i in range (num):
    l = getInput()
    l_list.append(l)
    Polycarpus(l, con_list, rec_list, lost_list)
if con_list[0] == 'LIVE' and con_list[1] == 'DEAD' and len(l_list) != 3:
    print(l_list)
for i in range(len(con_list)):
    print(con_list[i])
