result=[]
def Perm(list, begin, end):
    if begin>=end:
        string=""
        for i in range(len(list)):
            string=string+str(list[i])
        result.append(string)
    else:
        for i in range(begin, end):
            temp=list[begin]
            list[begin]=list[i]
            list[i]=temp
            Perm(list, begin + 1, end)
            temp = list[begin]
            list[begin] = list[i]
            list[i] = temp

n=int(input())
k=int(input())
A=[i for i in range(1,n+1)]
Perm(A,0,n)
print(result[k-1])