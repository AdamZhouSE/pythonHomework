import sys
list=sys.stdin.readline().split(",")
target=input()
list[0]=list[0][2]
for i in range(1,len(list)):
    list[i]=list[i][2]
list.sort()
jud=False
for item in list:
    if item>target:
        print(item)
        jud=True
        break
if not jud:
    print(list[0])