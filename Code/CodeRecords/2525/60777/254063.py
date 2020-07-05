temp=input()
temp=temp[1:len(temp)-1]
start=[int(x) for x in temp.split(',')]
temp=input()
temp=temp[1:len(temp)-1]
end=[int(x) for x in temp.split(',')]
temp=input()
temp=temp[1:len(temp)-1]
profit=[int(x) for x in temp.split(',')]

def pay(x):
    most=0
    for i in range(len(start)):
        if(start[i]>=x):
            temp=profit[i]+pay(end[i])
            if(temp>most):
                most=temp
    return most

res=0
for i in range(len(start)):
    if(pay(start[i])>res):
        res=pay(start[i])
        
print(res)