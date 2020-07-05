list_input = input().split("\"")
string1 = list_input[1]
string2 = list_input[3]
if len(string1) != len(string2):
    print("false")
    exit(0)
else:
    list1 = []
    list2 = []
    for i in range(len(string1)):
        list1.append(string1[i])
        list2.append(string2[i])
    list2.sort()
    list1.sort()
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print("false")
            exit(-1)
    print("true")
