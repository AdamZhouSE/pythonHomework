def Test():
    s=input()
    FU=False
    if(s.startswith("-")):
        FU=True
        s=s[1:]
    line=list(s)
    newline=[]
    for i in range(0,len(line)):
        newline.append(line[len(line)-i-1])
    result="".join(newline)
    while(result.startswith("0")):
        result=result[1:]
    if(FU):
        result="-"+result
    print(result)


if __name__ == "__main__":
    Test()