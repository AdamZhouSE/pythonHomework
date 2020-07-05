cases=[]
for _ in range(int(input())):
    cases.append(int(input()))
    binary=bin(cases[-1])[2:]
    while len(binary)!=32:
        binary="0"+binary
    result=""
    for i in binary:
        if i=="1":
            result+="0"
        else:
            result+="1"
    print(int(result,2))