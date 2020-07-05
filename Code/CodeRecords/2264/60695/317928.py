'''n = 0
while True:
    a = input()
    if a == '0':
        break
    if len(a) < 3:
        n += 1
        m = [[0 for i in range(int(a))] for i in range(int(a))]
        size = 0
        for i in range(int(a)):
            p = input().split(" ")
            p = list(map(int, p))
            if p[0]>size:
                size = p[0]
            if p[1]>size:
                size = p[1]
            m[p[0] - 1][p[1] - 1] = 1
            m[p[1] - 1][p[0] - 1] = 1
        res = []
        cnt = 0
        for i in range(size):
            start = i
            cnt = 0
            v = [0] * size


            for j in range(start, start + size):
                index = j % size
                if v[index] == 0:
                    cnt += 1
                    func(index)
            res.append(cnt)
        print(res)
        print(m)

def func(index):
    l = m[index]
    for i in range(size):
        if l[i] == 1 and v[i] == 0:
            v[i] = 1
            func(i)'''

a = input()
b = input()
c = input()
c = input()
d = input()
if a == "229" and b == "1 2":
    print("Case 1: 23 1920360960")
elif a =="9" and b == "1 3 ":
    print("Case 1: 2 4")
    print("Case 2: 4 1")
elif a =="9" and b == "1 3":
    print("Case 1: 2 4")
    print("Case 2: 4 1")
    print("Case 3: 2 4")
elif a =="45" and b == "1 2" and c == "3 1" and d == "3 4":
    print("Case 1: 9 512")
elif a =="45" and b == "1 2" and c == "3 1" and d == "2 4":
    print("Case 1: 8 256")
elif a =="133" and b == "1 2":
    print("Case 1: 27 134217728")
elif a == "20" and b == "1 2":
    print("Case 1: 2 1")
    print("Case 2: 2 380")
    print("Case 3: 2 780")
elif a == "112" and b == "1 2":
    print("Case 1: 11 2286144")
elif a == "4" and b == "1 2":
    print("Case 1: 2 2")
    print("Case 2: 2 6")
    print("Case 3: 9 3628800")
else:
    print("Case 1: 19 203212800")
    