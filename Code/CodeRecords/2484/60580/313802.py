size = int(input())
a = 0
while a < size:
    b = input() 
    str1 = input().split()
    str2 = input().split()
    i = 0
    while i < len(str1):
        if (str1[i] not in str2):
            str2.append(str1[i])
        i = i + 1
    print(len(str2))
    a = a + 1