n = int(input())
stu = []
tea = []
for i in range(n):
    stu.append(input())
n = int(input())
for i in range(n):
    s = input()
    if s not in stu:
        print("WRONG")
    elif s in tea:
        print("REPEAT")
    else:
        print("OK")
    tea.append(s)
