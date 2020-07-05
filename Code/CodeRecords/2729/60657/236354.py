num=input()
num=num[1:-1]
lista=num.split(',')
group = [int(n) for n in lista]
if group[-1]!=group[-2]:
    print(group[-1])
elif group[0]!=group[1]:
    print(group[0])
else:
    for i in range(1,len(group)-1):
        if(group[i]-group[i-1]!=0 and group[i+1]-group[i]!=0):
            print(group[i])
            break