import math
def min_reverse(str):
    if len(str)%2 == 1:
        return -1
    count_left = 0
    count_right = 0
    for i in range(len(str)):
        if str[i] == '{':
            count_left += 1
        else:
            if count_left > 0:
                count_left -= 1
            else:
                count_right += 1
    return math.ceil(count_left/2) + math.ceil(count_right/2)
            

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        ans.append(min_reverse(str))
    for res in ans:
        print(res)