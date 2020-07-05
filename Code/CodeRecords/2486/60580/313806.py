size = int(input())
a = 0
while a < size:
    str1 = input()
    l = []
    i = 0
    result = ""
    while i < len(str1):
        if str1[i] != ']':
            l.append(str1[i])
        else:
            temp = l.pop()
            while temp != '[':
                if temp.isalpha():
                    result = temp + result
                if temp.isdigit():
                    result = result * int(temp)
                temp = l.pop()
        i = i + 1
    if len(l) == 0:
        print(result)
    else:
        temp = l.pop()
        if temp.isdigit():
            result = result * int(temp)
        if temp.isalpha():
            result = temp + result
        print(result)
    a = a + 1