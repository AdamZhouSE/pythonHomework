def isLine(x1,y1,x2,y2,x3,y3):
    k1=(y1-y2)/(x1-x2)
    k2=(y2-y3)/(x2-x3)
    if k1==k2:
        return True
    else:
        return False

def isALine(lis):
    for i in range(0,len(lis)-2):
        if not isLine(lis[i][0],lis[i][1],lis[i+1][0],lis[i+1][1],lis[i+2][0],lis[i+2][1]):
            return False
    return True

n=int(input())
lis=[]
for i in range(0,n):
    lis.append(list(map(int,input().split(","))))
    
print(isALine(lis))


'''
if isALine(lis):
    print("true")
else:
    print("false")
'''

'''
x=input()
y=input()

print(x)
print(y)
'''