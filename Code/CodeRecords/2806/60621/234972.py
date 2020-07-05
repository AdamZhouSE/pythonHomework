n=int(input())
i=0
cap,price=[],[]
# def step(b):
#     ans = 1;
#     temp = 1
#     for i in range(1, len(b)):
#         if (b[i - 1] < b[i]):
#             temp += 1
#         else:
#
#             break
#         ans = max(ans, temp)
#     return ans
for i in range(n):
    temp = [int(x) for x in input().split()]
    cap.append(temp[0])
    price.append(temp[1])
minum=price[0]
count=0
for i in range(n):
    minum=min(minum,price[i])
    count+=cap[i]*minum
print(count)








