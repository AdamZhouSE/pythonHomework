def judge(list1, list2):
    list1.sort()
    list2.sort()
    if list1[len(list1) - 1] < list2[0]:
        return True
    else:
        return False


ori = eval(input())
approN = 0
for i in range(1, len(ori)):
    if judge(ori[:i], ori[i:]):
        approN += 1
print(1 + approN)
