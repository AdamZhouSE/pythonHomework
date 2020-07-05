'''
N 辆车沿着一条车道驶向位于 target 英里之外的共同目的地。
每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。
一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。
此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
会有多少车队到达目的地?
'''


def carFleet(target, position, speed):
    #cars = sorted(zip(position, speed))
    #times = [float(target - p) / s for p, s in cars]
    position.sort()
    speed.sort()
    times = []
    for i in range(0, len(position)):
        if (speed[i] != 0):
            times.append(float(target - position[i]) / speed[i])
    ans = 0
    count = 0
    i = len(times)
    while i > 1:
        lead = times[i-1]
        i -= 1
        if lead < times[-1]:
            ans += 1  # if lead arrives sooner, it can't be caught
        else:
            times[-1] = lead  # else, fleet arrives at later time 'lead'
            count += 1

    return ans + count  # remaining car is fleet (if it exists)


target = int(input())
inp1 = input()
speed = inp1[1:len(inp1) - 1].split(',')
speed = list(map(int, speed))
inp2 = input()
position = inp2[1:len(inp2) - 1].split(',')
position = list(map(int, position))
res = int(carFleet(target, position, speed))
print(res)