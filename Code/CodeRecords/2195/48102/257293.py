def set_prime_count(left: int, right: int) -> int:
    count = 0
    for i in range(left, right+1):
        if judge(i):
            count += 1
    return count


def judge(num: int) -> bool:
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    count = 0
    while num != 0:
        if num & 0x1 == 1:
            count += 1
        num >>= 1
    return count in prime


t = int(input())
ans = []
for j in range(t):
    ls = input().split(' ')
    l_num = int(ls[0])
    r_num = int(ls[1])
    ans.append(set_prime_count(l_num, r_num))
for j in ans:
    print(j)
    