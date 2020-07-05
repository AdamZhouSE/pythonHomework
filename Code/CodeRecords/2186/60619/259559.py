def find(index):
    if index == 1:
        return 1
    else:
        return find(index-1) + int((index+1)*index/2)


t = int(input())
for ind in range(t):
    n = int(input())
    print(find(n))