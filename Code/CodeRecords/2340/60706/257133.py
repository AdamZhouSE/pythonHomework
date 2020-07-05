def trap(height):
        left = -1
        lens = len(height)
        for i in range(lens):
            if height[i] != 0:
                left = i
                break
        if left == -1:
            return 0

        sum = 0
        flag = False
        while left < lens - 1:
            right = left + 1
            tem = 0
            while right < lens:
                if height[left] <= height[right]:
                    _sum = height[left] * (right - left - 1) - tem
                    sum += _sum
                    left = right
                    break
                tem += height[right]
                right += 1
                if right == lens:
                    flag = True
            if flag:
                break

        if flag:
            _left = lens - 1
            while _left > left + 1:
                _right = _left - 1
                tem = 0
                while _right >= left:
                    if height[_left] <= height[_right]:
                        _sum = height[_left] * (_left - _right - 1) - tem
                        sum += _sum
                        _left = _right
                        break
                    tem += height[_right]
                    _right -= 1
        return sum
t=int(input())
for i in range(t):
    n=int(input())
    list=input().split(' ')
    num=[]
    for j in range(len(list)):
        num.append(int(list[j]))
    sum=trap(num)
    print(sum)
        