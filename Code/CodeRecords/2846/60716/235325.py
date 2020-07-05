num = int(input())
str = input().split(' ')
list = [ int(i) for i in str]
sets = set(list)
print(len(sets)) if not 0 in sets else print(len(sets)-1)