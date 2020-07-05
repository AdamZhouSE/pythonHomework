n=float(input())
letter_list=list(input())
amount=0
for element in letter_list:
    if element=="A":
        amount+=4
    elif element=="B":
        amount+=3
    elif element=="C":
        amount+=2
    elif element=="D":
        amount+=1
result=amount/n
if result==0:
    print(0,end="")
else:
    print('%.14f'%result,end="")