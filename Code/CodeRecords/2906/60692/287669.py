n = int(input())
s = list(input())
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
for i in range(len(s)):
    s[i] = list1[(list1.index(s[i]) + n) % 26]
print("".join(s))