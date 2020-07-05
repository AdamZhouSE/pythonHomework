size = int(input())
a = 0
no = ["a", "e", "i", "o", "u"]
while a < size:
    b = input()
    i = 0
    l = []
    while i < len(b):
        if b[i] not in l and b[i] not in no:
            l.append(b[i])
        i = i + 1
    if len(l) % 2 == 0:
        print("SHE!")
    else:
        print("HE!")
    a = a + 1