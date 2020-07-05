def cal(s):
    count = 0
    for x in s:
        count += ord(x)
    return count

temp = input().split(" ")
s = temp[2].split(",")[0]
t = temp[5]

result = cal(s)==cal(t)
if result:
    print("true")
else:
    print("false")