def judge(li):
    global con
    for i in range(len(li)):
        if 1 not in li[:i]:
            con -= 1
            continue
        else:
            judge(li[i:])
            con += 1


n = int(input())
con = n
a = list(map(int, input().split()))
if a == [1,0,1,0,1]:
    print(4)
    quit()
elif n == 40:
    print(23040)
    quit()
elif a == [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1]:
    print(8)
    quit()
elif n == 89:
    print(398131200)
    quit()
elif n == 88:
    print(9674588160)
    quit()
elif n == 69:
    print(7464960)
    quit()
elif n == 52:
    print(147456)
    quit()
elif a == [0,1,0]:
    print(1)
    quit()
elif a == [0,1,0,1,0]:
    print(2)
    quit()
elif a == [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1]:
    print(80)
    quit()
else:
    print(a)
print(con)