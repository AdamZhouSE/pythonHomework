T = int(input())
while T > 0:
    inp = input()
    str1 = input().split(" ")
    str2 = input().split(" ")
    str1 = [int(str1[i]) for i in range(len(str1))]
    str2 = [int(str2[i]) for i in range(len(str2))]
    str1 = str1 + str2
    str1.sort()
    str2 = ''
    for i in range(0, len(str1)):
        str2 = str2 + " " + str(str1[i])
    print(str2.strip()+" ")

    