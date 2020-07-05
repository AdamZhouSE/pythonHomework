n=int(input())
arr=list(map(str,input().split()))
string=[]

for item in arr:
    record=[]
    num=0
    string.append(item)
    # string+=item
    for i in range(0,len(string)):
        for j in range(0,len(arr)-i):
            if j+i<len(string):
                # temp=string[j:j+i+1]
                temp="".join(string[x] for x in range(j,j+i+1))
                if (temp in record)==False:
                    num+=1
                    record.append(temp)
    print(num)