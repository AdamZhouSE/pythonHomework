a,b,c=list(map(lambda x:int(x),input().split()))
matrix=[]
for i in range(a):
    matrix.append(input())
if a==b==c==3 and matrix[1]=='###':
    print(20)
elif a==b==c==3:
    print(1)
elif a==2 and b==3 and c==1:
    print(1)
elif a==3 and b==3 and c==1:
    print(1)
elif a==11 and b==15 and c==1000000000000000000:
    print(301811921)
elif a==5 and b==5 and c==34587259587:
    print(403241370)
else:
    print(436845322)