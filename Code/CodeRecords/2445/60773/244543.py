dic={
    'a':1,
    'b':2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}
l1=[0]*26
l2=[0]*26
s=input().split(",")
s1=s[0][5:len(s[0])-1]
s2=s[1][6:len(s[1])-1]
for i in s1:
    l1[dic[i]]=l1[dic[i]]+1
for j in s2:
    l2[dic[j]]=l2[dic[j]]+1
if l1==l2:
    print("true")
else:
    print("false")