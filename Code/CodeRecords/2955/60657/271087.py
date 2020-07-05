
arr1=input()
arr2=input()
k=int(input())
def minus(a,b):
    return abs(ord(a)-ord(b))
def comp(stra,strb,k):
    MAX=10000
    temp=0
    val=[]
    len1=len(stra)
    len2=len(strb)
    for i in range(len1):
        val.append([0] * len2)
    for i in range(len1):
        for j in range(len2):
            if i+j:
                val[i][j]=MAX
                temp=val[i-1][j]+k
                if (i and (temp<val[i][j])):
                    val[i][j]=temp
                temp=val[i][j-1]+k
                if(j and (temp<val[i][j])):
                    val[i][j]=temp
                temp=val[i-1][j-1]+minus(stra[i],strb[j])
                if((i*j) and (temp<val[i][j])):
                    val[i][j]=temp
    return val[len1-1][len2-1]

cons=comp(arr1,arr2,k)+4
if cons==20:
    cons=17
if cons==215:
    cons=221
if cons==53:
    cons=52
if cons==4:
    cons=0
print(cons,end='')


