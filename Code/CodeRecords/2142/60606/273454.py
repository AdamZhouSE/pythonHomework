
test_num = int(input())
for i in range(test_num):
    left = []
    s = input()
    s = list(s)
    index_left = 1
    for j in range(len(s)):
        if s[j] == "(":
            s[j] = str(index_left)
            index_left += 1
    for j in range(len(s)):
        if s[j] == ")":
            for k in range(j-1,-1,-1):
                if type(s[k]) == str and ord(s[k]) >= ord("1") and ord(s[k]) <= ord("9"):
                    s[j] = int(s[k])
                    s[k] = int(s[j])
                    break
    for item in s:
        if type(item) == int or ord(item) >= ord("1") and ord(item) <= ord("9"):
            print(item,end=" ")
    print()




