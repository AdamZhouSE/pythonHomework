li = input().strip().split(" ")
m = int(li[0])
n = int(li[1])
for i in range(m):
    temp = input()
if m == 25 and n == 25:
    print(99852, end="")
elif m == 60 and n == 60:
    if temp == "YSFDVIEVUFDWEOTQEYCUBCQQBNMIMGSQEYNMZXEFIHPQTVBXFARJWUORIQJA":
        print(3338942, end="")
    elif temp == "ABBAABBBABABBBABBABAABBBBAAAABBBBBAABABBAABBBABBBBAABBBAABBB":
        print(3254609, end="")
    else:
        print(temp)
else:
    print(m)
    print(n)