#24
import math

ori = input().split(" ")
n = int(ori[0])
root = int(ori[1])

flag1 = True
for i in range(0,n):
    ori = input().split(" ")
    root = int(ori[0])
    lch = int(ori[1])
    rch = int(ori[2])
    if lch != 0 and lch > root:
        flag1 = False
    if rch != 0 and rch < root:
        flag1 = False

if flag1 == True:
    print("true")
else:
    print("false")

total = 0
flag2 = False
for i in range(0,10):
    total += pow(2,i)
    if total == n:
        flag2 = True
        break

if flag2:
    print("true")
else:
    print("false")

# if flag2 == "false":
#     print("false")
#     print("false")
# 
# else:
#     if flag1:
#         print("true")
#     else:
#         print("false")
#     print("true")

