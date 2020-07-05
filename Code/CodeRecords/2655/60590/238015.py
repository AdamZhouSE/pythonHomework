tests = int(input())

lists = []
for i in range(tests):
    a = int(input())
    lists.append(a)
#print(lists)

def judge(num):
    num = int(num)
    if num==0 or (num & num-1)==0:
        return True
    else:
        return False

for i in range(lists.__len__()):
    base = lists[i]
    while not judge(base):
        base += 1
    print(base)