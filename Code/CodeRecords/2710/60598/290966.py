line = input().split(" ")
student = int(line[0])
question = int(line[1])
result = []
for i in range(question):
    temp = input().split(" ")
    if temp[0] == "M":
        result.append([int(temp[1]), int(temp[2])])
    else:
        station = int(temp[1])
        age = int(temp[2])
        Min = 100000000
        sta = 0
        for re in result:
            if re[0] <= station and re[1] >= age:
                if Min > re[1]:
                    Min = re[1]
                    sta = re[0]
        if Min == 100000000:
            print(-1)
        else:
            print(Min)
