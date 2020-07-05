def judge(n):
    if len(n) == 1 or len(n) == 2 or len(n) == 0:
        return True
    else:
        target = n[len(n) - 1]
        index = 0
        while index < len(n):
            if n[index] >= target:
                break
            index += 1
        for i in range(index, len(n)-1):
            if n[i] < target:
                return False
        return judge(n[:index]) and judge(n[index:len(n)-1])


length = int(input())
try:
    numbers = [int(i) for i in input().strip().split(" ")]
    if judge(numbers):
        print("true")
    else:
        print("false")
except EOFError as err:
    print("true")
