length=0
key=""
for i in input().split():
    if len(i)>length:
        key=i
        length=len(i)
print(key)