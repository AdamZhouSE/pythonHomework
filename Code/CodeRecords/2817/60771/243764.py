#30
n = int(input())
ori = input().split(" ")
num = [int(item) for item in ori]
name = [i+1 for i in range(0,n)]
hasFriend = False
for i in range(0,n-2):
    name_one = num[i]
    name_two = num[name_one-1]
    name_three = num[name_two-1]
    if name[i] == name_three:
        hasFriend = True
        break
if hasFriend:
    print("YES")
else:
    print("NO")