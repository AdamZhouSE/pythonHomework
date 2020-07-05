import copy

n = int(input())
arrange = []
for i in range(0,n):
    operation = input()
    if(operation[0] == 'B'):
        print(len(arrange))
    elif(operation[0] == 'A'):
        op = operation.split()
        l = int(op[1])
        r = int(op[2])
        temp = []
        for conf in arrange:
            if(conf[0] > r or conf[1] < l):
                temp.append(conf)
        print(len(arrange) - len(temp))
        
        temp.append([l,r])
        arrange = copy.deepcopy(temp)
        