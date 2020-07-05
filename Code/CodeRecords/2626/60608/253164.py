def computeCoin(balloons: list, target: int, num: int, coin: int):
    if num == target:
        if coin > balloons[0]:
            balloons[0] = coin
    else:
        for i in range(1, target):
            if balloons[i] >= 0:
                val = balloons[i]
                balloons[i] = -1

                # get left num
                left = i - 1
                while left > 0 and balloons[left] < 0:
                    left -= 1
                leftNum = 1 if left <= 0 else balloons[left]

                # get right num
                right = i + 1
                while right < target and balloons[right] < 0:
                    right += 1
                rightNum = 1 if right >= target else balloons[right]

                tem = val * leftNum * rightNum
                computeCoin(balloons, target, num + 1, coin + tem)
                balloons[i] = val


def func34():
    balloons = [0] + list(eval(input()))
    computeCoin(balloons, len(balloons), 1, 0)
    print(balloons[0])
    if balloons[0]==0:
        print(balloons)


func34()
