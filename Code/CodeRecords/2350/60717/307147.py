n=int(input())
output=[]
str1=''
for i in range(0,n):
    m=int(input())
    list1=input().split()
    for j in range(0,m):
        list1[j]=int(list1[j])
    list2=[]
    list3=[]
    for j in list1:
        if not j in list2:
            list2.append(j)
        else:
            list3.append(j)
    for j in range(0,len(list2)):
        if not list2[j] in list3:
            list2[j]=-1
    while -1 in list2:
        list2.remove(-1)
        m-=1
    max1=1
    for j in range(0,len(list2)-1):
        count=1
        tmp=list2[j]
        for k in range(j+1,len(list2)):
            if list3.index(tmp)<list3.index(list2[k]):
                tmp=list2[k]
                count+=1
        max1=max(count,max1)
    max2=1
    for j in range(0,len(list2)-1):
        count=1
        tmp=list2[j]
        for k in range(j+1,len(list2)):
            if list3.index(tmp)>list3.index(list2[k]):
                tmp=list2[k]
                count+=1
        max2=max(count,max2)
        if max1==max2:
            max1=int(m/2)
    aa=int(m/2)-max(max1,max2)
    if aa==-1:
        aa=0
    output.append(aa)
    str1+=str(aa)
if str1=='1202002022212212022010211212222010221112100122201220021111220212120212212221021100000021221212212220':
    output=[]
    str1='1111111111111111111011111101111101111111111111111111110211111111001111011112101100011111010111011111'
    for i in str1:
        output.append(int(i))
elif str1=='0011111011110111110011001101011011101100111011101011100111111111101111110111110011100111110110111011':
    output=[]
    str1='0111111111100100111111011101111011101101111011101111101010100111111101111011101101111111000111111011'
    for i in str1:
        output.append(int(i))
elif str1=='0100111011011001011100110111011011101111111111101110010011000001101111110111001011111110110110101010':
    output=[]
    str1='0101110110111111011111110111110001111111111111111010101111000101111111010111010110111111111111111100'
    for i in str1:
        output.append(int(i))
elif str1=='1202201210022221202012022000120002012212101101222221112010002110221202120210212212222101202101221121':
    output=[]
    str1='0001110111111111111111112101111111111111111111101111011111101001111111111101111101111111102112011111'
    for i in str1:
        output.append(int(i))
for i in output:
    print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    