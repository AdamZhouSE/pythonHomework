arr = eval(input())

def do(lis):
    if lis[-1] == len(lis)-1:
        return 1 + do(lis[:len(lis)-1])
    else:
        return 0

print(do(arr)+1)