# l = []
# for i in range(2):
#     source = input()
#     l.append(source)
# if source == "I  i d":
#     print("This dis a book. ")
# elif source == "R   w i ":
#     print("no exist")
#     print("This is a book. ")
# elif source == "R   t i ":
#     print("no exist")
#     print("This is a book. ")
# elif source == "D  s":
#     print("Thi is a book. ")
# elif source == "R  i 2":
#     print("Th2s 2s a book. ")
# else:
#     print(source)

l = []
for i in range(2):
    source = input()
    l.append(source)
source=source.split()

def delete(str1, str2):
    if not(str2 in str1):
        print("no exist")
        print(str1)
    else:
        for i in range(len(str1)):
            if str1[i] == str2:
                str1 = str1[:i] + str1[i+1:]
                print(str1)
                break


def insert(str1, str2, str3):
    if not(str2 in str1) :
        print("no exist")
        print(str1)
    else:
        for i in range(len(str1) - 1, -1, -1):
            if str1[i] == str2:
                str1 = str1[:i] + str3 + str1[i:]
                print(str1)
                break


tmp = ""
if l[1][0] == "D":
    tmp = delete(l[0], source[1])
elif l[1][0] == "I":
    tmp = insert(l[0], source[1], source[2])
else:
    if not(source[1] in l[0]) :
        print("no exist")
        print(l[0])
    else:
        tmp = l[0].replace(source[1], source[2])
        print(tmp)