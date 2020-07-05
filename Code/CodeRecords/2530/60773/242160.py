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
quence=[26]*26
s1=input()
s2=input()
list=list(s2)
for i in range(len(s1)):
    quence[dic[s1[i]]-1]=i
#print(quence)
for i in range(0,len(s2)-1,1):
    for i in range(0,len(s2)-1,1):
        # print(quence[dic[s2[i]]-1])
        # print(quence[dic[s2[i+1]]-1])
        if (quence[dic[list[i]]-1])>(quence[dic[list[i+1]]-1]):
            t=list[i+1]
            list[i+1]=list[i]
            list[i]=t
result=""
for i in list:
    result=result+i
print(result)