def find(str1,str2):
    num = 0
    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                break
        else:
            num = num + 1
    return num

inputs = input()
outputs = []
groove = ""
for letter in inputs:
    if letter == "P":
        outputs.append(groove)
    elif letter == "B":
        groove = groove[:-1]
    else:
        groove = groove + letter
numOfSearch = int(input())
for i in range(numOfSearch):
    search = input().split(" ")
    str1 = int(search[0])-1
    str2 = int(search[1])-1
    if str1>=len(outputs) or str2>=len(outputs):
        print(0)
    else:
        print(find(outputs[str1],outputs[str2]))