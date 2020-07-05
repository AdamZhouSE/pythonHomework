n=input()
count=0
res=''
for i in range(len(n)):
    if count==0 :
        if int(n[len(n)-i-1])>=1 and int(n[len(n)-i-1])<=3:
            for i in range(int(n[len(n)-i-1])):
                res='I'+res
        elif int(n[len(n)-i-1])>=5 and int(n[len(n)-i-1])<=8:
            for i in range(int(n[len(n)-i-1])-5):
                res='I'+res
            res='V'+res
        elif int(n[len(n)-i-1])==4:
            res='IV'+res
        elif int(n[len(n)-i-1])==9:
            res='IX'+res
    elif count==1 :
        if int(n[len(n)-i-1])>=1 and int(n[len(n)-i-1])<=3:
            for i in range(int(n[len(n)-i-1])):
                res='X'+res
        elif int(n[len(n)-i-1])>=5 and int(n[len(n)-i-1])<=8:
            for i in range(int(n[len(n)-i-1])-5):
                res='X'+res
            res='L'+res
        elif int(n[len(n)-i-1])==4:
            res='XL'+res
        elif int(n[len(n)-i-1])==9:
            res='XC'+res
    elif count==2 :
        if int(n[len(n)-i-1])>=1 and int(n[len(n)-i-1])<=3:
            for i in range(int(n[len(n)-i-1])):
                res='C'+res
        elif int(n[len(n)-i-1])>=5 and int(n[len(n)-i-1])<=8:
            for i in range(int(n[len(n)-i-1])-5):
                res='C'+res
            res='D'+res
        elif int(n[len(n)-i-1])==4:
            res='CD'+res
        elif int(n[len(n)-i-1])==9:
            res='CM'+res
    elif count==3 :
        if int(n[len(n)-i-1])>=1 and int(n[len(n)-i-1])<=3:
            for i in range(int(n[len(n)-i-1])):
                res='M'+res
    count=count+1
print(res)