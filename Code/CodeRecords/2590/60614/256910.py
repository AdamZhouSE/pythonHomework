num=int(input())
problems=[]
for i in range(num):
    problems.append(input())
for i in problems:
    temp=list(i)
    j=0
    while j!=len(temp):
        if temp.count(temp[j])>1 or temp[j] in 'aeiou':
            temp.remove(temp[j])
            j-=1
        j+=1
    if len(temp)%2==1:
        print('HE!')
    else:
        print('SHE!')