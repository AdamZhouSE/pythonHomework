num=int(input())
c= 0
grade = input()
for i in range(num):
    if grade[i] == "A":
        c=c+4
    elif grade[i] == "B":
        c=c+3
    elif grade[i] == "C":
        c=c+2
    elif grade[i] == "D":
        c=c+1
    else:
        c=c+0
gpa = c/num
if gpa == 0:
    print('0',end='')
else:
    print('%.14f'%gpa,end='')