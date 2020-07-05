import math
#转化为26进制,没有0 A作为0
result = []
output = []
num = int(input())
while num != 0:
    result.append(num%26)
    num = math.floor(num/26)
result.reverse()
for item in result:
    output.append(chr(item+ord("A")-1))
STR = "".join(output)
STR = STR.replace("A@","Z")
print(STR)


