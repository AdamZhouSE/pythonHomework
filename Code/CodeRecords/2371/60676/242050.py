def palindrome(string_array):
    temp = True
    for i in range(len(string_array)//2):
        if string_array[i] != string_array[-i-1]:
            temp = False
    if temp:
        return 'YES'
    return 'NO'


result = []
for i in range(int(input())):
    raw_str = input()
    new_str = []
    for j in range(len(raw_str)):
        if raw_str[j].islower():
            new_str.append(raw_str[j])
        elif raw_str[j].isupper():
            new_str.append(raw_str[j].lower())
        else:
            continue
    result.append(palindrome(new_str))
for i in range(len(result)):
    print(result[i])