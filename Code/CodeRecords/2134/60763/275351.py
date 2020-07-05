import math
buckets = int(input())
minutesToDie = int(input())
minutesToTest = int(input())
k = math.ceil(minutesToTest / minutesToDie)
k = int(minutesToTest / minutesToDie)
# print(k)
i = 1
t = buckets
while pow(k+1,i)<buckets:
    i+=1
# while t > pow(2,i):
#     t = buckets
#     for j in range(k-1):
#         t = math.ceil(t/i)
#     i+=1
print(i)