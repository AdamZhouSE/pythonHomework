num=int(input())
for i in range(num):
    str=input()
    patt=input()
    judge=True
    for j in str:
        if j in patt:
            print(j)
            judge=False
            break
    if judge:
        print("$")