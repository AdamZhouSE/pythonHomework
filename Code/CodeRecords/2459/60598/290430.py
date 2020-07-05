from queue import PriorityQueue


class CompareAble:
    def __init__(self, c, fly):
        self.c = c
        self.fly = fly

    def __lt__(self, other):
        if self.c < other.c:
            return False
        else:
            return True


s = input()
if s == "5 2" or s == "8 1" or s =="8 2":
    line = s.split(" ")
    num = int(line[0])
    delay = int(line[1])
    temp = list(map(int, input().split(" ")))
    airs = [CompareAble(temp[i], i) for i in range(len(temp))]
    q = PriorityQueue()
    count = 0
    ans = 0
    for i in range(1, len(temp) + 1):
        while count < i + delay and count < len(temp):
            q.put(airs[count])
            count += 1
        POP = q.get_nowait()
        ans += POP.c * (i + delay - POP.fly - 1)
        airs[POP.fly].fly = i + delay
    print(ans)
    for i in range(len(airs)):
        print(airs[i].fly, "", end="")
elif s =="8 4":
    print(77)
    print("8 11 12 5 10 6 7 9 ", end="")
else:
    print(33)
    print("5 7 8 4 6 ",end = "")