def another(m):
    return m[1]

n = eval(input())
computer = []
while(n != 0):
    n = n - 1
    computer.append(list(map(int,input().split(" "))))
computer.sort()
computer1 = computer.copy()
computer1.sort(key=another)

if(computer1 == computer):
    print("Poor Alex")
else:
    print("Happy Alex")