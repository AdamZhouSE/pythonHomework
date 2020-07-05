a = input()
l1 = input().split()
l2 = input().split()
temL = []
for val in l2:
    if val in l1:
        temL.append(val)
result = ""
for val in l1:
    if val in temL:
        result = result + val + " "
print(result.strip())