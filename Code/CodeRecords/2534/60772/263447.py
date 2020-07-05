str = input()
arr = []
for ele in str:
    if ele.isdigit():
        arr.append(int(ele))
arr.sort()
print(arr)