s = input()
arr = []
for ele in s:
    if ele.isdigit():
        arr.append(int(ele))
arr.sort()
print(arr)