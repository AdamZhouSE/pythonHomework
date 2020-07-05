str = input()
result=[]
for x in list(str):
    try:
        result.append(int(x))
    except:
        pass
result.sort()
print(result)