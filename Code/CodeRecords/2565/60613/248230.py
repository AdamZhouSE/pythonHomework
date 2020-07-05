s1=input()
s2=input()


if len(s1)==0 or s1.isspace():
    lst1=[]
else:
    lst1 = list(map(int, s1.split(",")))
if len(s2)==0 or s2.isspace():
    lst2=[]
else:
    lst2 = list(map(int, s2.split(",")))

LEN = len(lst1) + len(lst2)
middle = 0
if LEN % 2 == 0:
    middle = LEN // 2 - 1
else:
    middle = LEN // 2

i, j, curr, first, second = [0, 0, -1, 0, 0]

while i < len(lst1) and j < len(lst2):
    currVal =0
    if lst1[i] <= lst2[j]:
        currVal = lst1[i]
        i += 1
    else:
        currVal = lst2[j]
        j += 1
    curr += 1
    if middle == curr:
        first = currVal
    if middle + 1 == curr:
        second = currVal

if curr < middle + 1:
    if len(lst1) == i:
        while j < len(lst2):
            currVal = lst2[j]
            j+=1
            curr += 1
            if middle == curr:
                first = currVal
            if middle + 1 == curr:
                second = currVal
                break
    else:
        while i < len(lst1):
            currVal = lst1[i]
            i+=1
            curr += 1
            if middle == curr:
                first = currVal
            if middle + 1 == curr:
                second = currVal
                break
if LEN % 2 == 0:
    print(format((first + second) / 2,"0.5f"))
else:
    print(format(first,"0.5f"))







