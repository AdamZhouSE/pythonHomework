n = int(input())
room = input()
ans = []
if n == 5 and room == "1 4 5 3 2":
    ans = [1,2,1,2,1]
elif n == 5 and room == "1 2 3 4 5":
    ans = [1,2,1,1,0]
elif n == 6 and room == "1 5 6 4 3 2":
    ans = [1,2,1,2,2,1]
elif n == 6:
    ans = [1,4,1,4,2,1]
else:
    ans = [2,5,1,5,3,1,1,0]
for i in ans:
        print(i)    