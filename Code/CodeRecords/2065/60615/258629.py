string=input()

def atoi(string):
    num=['1','2','3','4','5','6','7','8','9','0']
    token=[i for i in string]
    valid=''
    start=False
    for tok in token:
        if tok !=' ':
            start=True
        if start:
            if tok=='+' or tok=='-' or tok in num:
                valid=valid+tok
            else:
                start=False
                break
    if valid=='':
        return 0
    else:
        valid=int(valid)
        if valid>2147483648 or valid<-2147483648:
            if valid>2147483648:
                valid=2147483648
            else:
                valid=-2147483648
        return valid

result=atoi(string)
print(result)
