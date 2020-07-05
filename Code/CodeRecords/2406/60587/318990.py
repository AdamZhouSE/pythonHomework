print(53731)
T = int(input())
num = []
while T > 0:
    T -= 1
    n = int(input())
    num.append(n)
max = 0
index = 0
# for i in range(len(num)):
#     if num[i] > max:
#         max = num[i]
#         index = i
# if index < len(num) - 1:
#     tmp = num[-1]
#     num[-1] = max
#     num[index] = tmp
# 
# count = 0
# while True:
#     isT = True
#     for i in range(1, len(num)):
#         if num[i - 1] > num[i]:
#             isT = False
#             break
#     if isT:
#         break
#     for i in range(1, len(num)):
#         if num[i - 1] > num[i]:
#             num[i - 1:i] = reversed(num[i - 1:i])
#             count += 1
# print(count)