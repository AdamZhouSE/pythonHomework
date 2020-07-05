lists=list(map(int,input().split(',')))
def func(lists:list):
    for i in range(int(len(lists)/4)):
        if lists[4*i+2]<=lists[4*i] and lists[4*i+3]>=lists[4*i+1]:
            return True
    return False
print(func(lists))