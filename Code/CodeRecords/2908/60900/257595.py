n = input()
result = []
for i in range(0,int(n)):
    result.append(''.join(sorted(input())).replace(" ",""))

print(len(list(set(result))),end='')