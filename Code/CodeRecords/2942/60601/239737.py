n = eval(input())
num = input().split(' ')
num.sort(reverse=True)
print("".join(num),end='')