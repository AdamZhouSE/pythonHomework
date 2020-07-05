s = input()
current_str = ''
output = []
for i in range(len(s)):
    if s[i] == 'B':
        current_str = current_str[:-1]
    elif s[i] == 'P':
        output.append(current_str)
    else:
        current_str += str(s[i])

n = int(input())
for i in range(n):
    arr = input().split()
    str1 = output[int(arr[0]) - 1]
    if int(arr[1]) > len(output):
        print(0)
        continue
    str2 = output[int(arr[1]) - 1]
    temp = len(str1)
    count = 0
    for j in range(len(str2)):
        if j + temp <= len(str2) and str1 == str2[j:j+temp]:
            count += 1
    print(count)
