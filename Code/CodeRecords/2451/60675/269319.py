def fun(list,target):
    for i in range(len(list)):
        if target <= int(list[i]):
            return i
    return len(list)

n = input()
m = input()
target = int(m)
list = n.split(",")
print(fun(list,target))