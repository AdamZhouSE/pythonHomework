import operator
def compare(s1,s2):
    dic = {
        'A': '0',
        'B': '1',
        'C': '2',
        'D': '3',
        'E': '4',
        'F': '5',
        'G': '6',
        'H': '7',
        'I': '8',
        'J': '9',
        'K': '10',
        'L': '11',
        'M': '12',
        'N': '13',
        'O': '14',
        'P': '15',
        'Q': '16',
        'R': '17',
        'S': '18',
        'T': '19',
        'U': '20',
        'V': '21',
        'W': '22',
        'X': '23',
        'Y': '24',
        'Z': '25',
    }
    if len(s1)!=len(s2):
        return False
    list1=[0]*26
    list2=[0]*26
    for i in s1:
        list1[int(dic[i])]=list1[int(dic[i])]+1
    for i in s2:
        list2[int(dic[i])]=list2[int(dic[i])]+1
    return operator.eq(list1,list2)

n=int(input())
list=[]
for i in range(n):
    
    list.append(input().split(" ")[0])
#print(list)
result=[]
result.append(list[0])
sum=1
for i in list:
    flag=0
    for j in result:
        if compare(i,j):
            flag=flag+1
    if(flag==0):
        result.append(i)
        sum=sum+1
print(sum,end="")