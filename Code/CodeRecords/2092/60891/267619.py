

def is_told(l):
    for i in range(len(l)):
        if l[i].count(i) >= 2:
            return True
    return False


n = int(input())
t = [(int(i) - 1) for i in input().split()]
info_list = [[i] for i in range(n)]
count = 0
'''
注意啊，告诉的时候是同时告诉的
'''
while not is_told(info_list):
    count += 1
    info_list_copy = [x[:] for x in info_list]
    for i in range(n):
        tmp = info_list_copy[i]
        for j in tmp:
            info_list[t[i]].append(j)
print(count)