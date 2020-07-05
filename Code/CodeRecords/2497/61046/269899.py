target = input()
positionList = input()
positionList = positionList.replace("[",'')
positionList = positionList.replace("]",'')
position = positionList.split(",")
position = list(map(int, position))
speedList = input()
speedList = speedList.replace("[",'')
speedList = speedList.replace("]",'')
speed = speedList.split(",")
speed = list(map(int, speed))

lst = sorted(zip(position, speed))
times = [(int(target) - int(p)) / int(s) for p, s in lst]
ans = 0

while len(times) > 1:
    lead = times.pop()
    if lead < times[-1]:
        ans += 1
    else:
        times[-1] = lead
        # 当times = 1时,不进入循环, 最后一队车没有可比较的对象, 没有+1, 所以此处需要+1
        # 当time = 0时, 不进入循环, 没有车队, 所以此处为0
        # 合并上述两项, 所以采用如下写法
print(ans+1)