input()
init=sorted([int(x) for x in input().split()])
key= init[0]
for i in init:
    if i%key!=0:
        key=-1
        break
print(key)