import math
test_num = int(input())
for k in range(test_num):
    s = input()
    string = []
    for i in s:
        if 'a'<=i and i<='z' and i<='A' and 'Z'<=i:
            string.append(i)
    s = "".join(string)
    s.capitalize()
    length = math.floor(len(s)/2)
    sentinel = 0
    for i in range(length):
        if string[i] != string[len(string) - i-1]:
            sentinel = 1
    if sentinel == 0:
        print("YES")
    else:
        print("NO")