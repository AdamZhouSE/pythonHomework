def solution(number):
    (number, flag) = divmod(number, 2)
    while number:
        (number, remainder) = divmod(number, 2)
        if remainder == flag:
            return False
        flag = remainder
    return True


num = int(input())
print(solution(num))
