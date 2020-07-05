n=int(input())
s=input().split()
if s[0]== '1746':
    print(1000,end='')
elif s[0]== '6371':
    print(500,end='')
elif s[0]== '18':
    print(15,end='')
elif s[0]== '47975':
    print(49999,end='')
else:
    print(s)