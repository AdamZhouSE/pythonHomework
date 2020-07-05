N=int(input())
expression=[]
for i in range(N):
    string=input().split(" ")
    if string[0]=="Add":
        ex=[]
        for j in range(1,len(string)):
            if string[j]!="":
                ex.append(int(string[j]))
        expression.append(ex)
    elif string[0]=="Del":
        index=int(string[1])
        expression[index-1]="*"
    else:
        k=int(string[1])
        result=0
        for j in range(len(expression)):
            if expression[j]!="*" and expression[j][0]*k+expression[j][1]>expression[j][2]:
                result+=1
        print(result)