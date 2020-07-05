def operation(string):
    string=[i for i in string]
    substring=[]
    for i in range(len(string)):
        for j in range(i,len(string)):
            substr=string[i:j+1]
            if len(substring)==0:
                substring.append(substr)
            else:
                judge=0
                for k in range(len(substring)):
                    if len(set(substring[k]+substr))==len(substring[k])+len(substr):
                        judge=1
                if judge==1:
                    substring.append(substr)
    sum=0
    for i in range(len(substring)):
        sum+=len(substring[i])
    return sum
t=int(input())
for i in range(t):
    n=int(input())
    string=input().split()
    print(operation(string))
    