def permutations(arr, position, end,oc):
    if position == end:
        m=""
        for index in range(len(arr)):
           m=m+arr[index]
        oc.append(m)
    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position+1, end,oc)
            arr[index], arr[position] = arr[position], arr[index]
s=input()
count=0
n=(int)(input())
for index in range(n):
    mima=(list)(input())
    oc=[]
    permutations(mima,0,len(mima),oc)
    mimaji=[]
    for index1 in range(len(s) - len(mima) + 1):
        for index2 in range(len(oc)):
            if s[index1:index1 + len(mima)] == oc[index2]:
                yiyou=False
                for index3 in range(len(mimaji)):
                    if mimaji[index3]==oc[index2]:
                        yiyou=True
                        break
                if yiyou==True:
                    break
                else:
                    count += 1
                    mimaji.append(oc[index2])
                    break
print(count)
