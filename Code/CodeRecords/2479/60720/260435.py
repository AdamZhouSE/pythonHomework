import string
size=int(input())
for i in range(size):
    str1=input()
    str2=input()
    for word in string.ascii_lowercase:
        if ((word in str1) and( word not in str2)) or ((word in str2) and (word not in str1)) :
            print(word,end='')
    print()
    print()