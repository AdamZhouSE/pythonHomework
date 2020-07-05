cases=[]
for _ in range(int(input())):
    cases.append(int(input()))
    binary=bin(cases[-1])[2:]
    result=""
    for i in binary:
        if i=="1":
            result+="0"
        else:
            result+="1"
    print(int(result,2))