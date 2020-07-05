num = int(input())
l = []
for i in range(num):
    l.append(input())
minlength = len(l[0])
tag = 0
for i in range(1, num):
    if len(l[i]) < minlength:
        minlength = len(l[i])
        tag = i


def maxsubchar(str1):
    sublength = 0
    t = 0
    for i in range(1, len(str1) + 1):
        for j in range(len(str1) - i + 1):
            t=0
            for k in range(len(l)):
                if not (str1[j:j + i] in l[k]):
                    t = 1
                    break
            if t == 0 and i > sublength:
                sublength = i
    return sublength


result = maxsubchar(l[tag])
print(result)