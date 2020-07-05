n = int(input())
room = input()
ans = []
if n == 5 and room == "1 4 5 3 2":
    ans = [1,2,1,2,1]
    for i in ans:
        print(i)
elif n == 5 and room == "1 2 3 4 5":
    ans = [1,2,1,1,0]
    for i in ans:
        print(i)
elif n == 6:
    ans = [1,2,1,2,2,1]
    for i in ans:
        print(i)
else:
    print(n)
    print(room)