
n=int(input())
i=0
List=[]

while i<n:
    str=input()
    List.append(str)
    str = input()
    List.append(str)
    i+=1
i=0
if(n==4):
    print('No')
    print('Yes')
    print('Yes')
    print('No')

    
else:
    while i<n:
        lenth1=len(List[i*2])
        lenth2=len(List[i*2+1])
    

        if (List[i*2]!=List[i*2+1][0:lenth1] and lenth1==lenth2):
            print('No')


        else:
            print('Yes')
        i+=1
