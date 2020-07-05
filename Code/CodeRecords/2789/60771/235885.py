#14
n = int(input())
for i in range(0,n):
    num = int(input())
    outcome = 1
    flag = True
    ori = input().split(" ")
    length = [int(item) for item in ori]
    length.sort()
    while flag:
        # print(outcome)
        if num-outcome <0:
            break
        for i in range(num-outcome,num):
            # print("i: "+str(i))
            # print("length: "+str(length[i]))
            if length[i] < outcome:
                flag = False
                break
        if flag:
            outcome+=1
    print(outcome-1) #前面多加了一次，要减掉