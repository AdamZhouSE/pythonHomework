s = input()
s = s[1:len(s) - 1]
li = s.split(",")
arr = []
for item in li:
    arr.append(int(item))
arr.sort()
print(arr)