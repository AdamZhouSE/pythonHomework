# 28
inp = input()
n = int(inp)
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
m = 0
def permutations(arr, position, end):
    global m
    if position == end:
        ok = True
        p = 0
        for i in range(len(arr)):
            if sum(num[:i]) <= num[i]:
                p += 1
        if p > m:
            m = p
            
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]
permutations(num,0,len(num))

print(m)