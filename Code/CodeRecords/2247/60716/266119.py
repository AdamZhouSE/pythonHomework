strs = input().split(',')
lists = [int(i) for i in strs]
print(lists)
alex = 0
lee = 0
index=0
while len(lists)>0:
    temp = 0
    if lists[0]>=lists[len(lists)-1]:
        temp = lists.pop(0)
    else:
        temp = lists.pop()
    if index%2==0:
        alex += temp
    else:
        lee += temp
print(True) if alex>lee else print(False)