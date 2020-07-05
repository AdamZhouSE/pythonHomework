tests=(int)(input())
for i in range(tests):
    string=input()
    record=-1
    for j in range(len(string)):
        for k in range(len(string)-1,j,-1):
            if(string[k]==string[j]):
                if(k-j-1>record):
                    record=k-j-1
                break
    print(record)