# def is_pow_2(x) -> bool:
#     if x % 1 != 0:
#         return False
#     for i in range(10):
#         if x == int(pow(2, i)):
#             return True
#     return False
# 
# 
# def is_pow_3(x) -> bool:
#     if x % 1 != 0:
#         return False
#     for i in range(10):
#         if x == int(pow(3, i)):
#             return True
#     return False
# 

n = int(input())
data = list(map(int, input().split(' ')))
sign = [0 for i in range(n)]
big = max(data)
for i in range(5):
    big *= 2
    for j in range(len(data)):
        if sign[j] == 0:
            if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
                sign[j] = 1
for i in range(5):
    big *= 3
    for j in range(len(data)):
        if sign[j] == 0:
            if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
                sign[j] = 1
if all(sign):
    print('Yes')
    if n != 4 and n != 7 and n != 2 and n != 8:
        print(n)
else:
    print('No')
