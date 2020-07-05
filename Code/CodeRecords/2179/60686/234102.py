def judge(arrJ, string):
    maximum = 0
    string1 = string[int(arrJ[0]) - 1:int(arrJ[1])]
    len1 = len(string1)
    string2 = string[int(arrJ[2]) - 1:int(arrJ[3])]
    len2 = len(string2)
    record = [[0 for x in range(len2 + 1)] for y in range(len1 + 1)]
    for j in range(0, len1):
        for k in range(0, len2):
            if string1[j] == string2[k]:
                record[j + 1][k + 1] = record[j][k] + 1
                if record[j + 1][k + 1] > maximum:
                    maximum = record[j + 1][k + 1]
    k = j = 0
    return maximum


n, m = input().split(" ")
arr = []
stringInput = input()
for i in range(0, int(m)):
    arr.append(input().split(" "))
for u in range(0, int(m)):
    print(judge(arr[u], stringInput))
