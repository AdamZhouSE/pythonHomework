n=int(input())
condition=eval(input())
subject=[]
for i in condition:
    subject+=i
subject=list(set(subject))
seq=[]
while(subject):
    s=subject[0]
    k=0
    for con in condition:
        if(s==con[0]):
            k=1
            break
    if(k==0):
        seq.append(s)
        temp=[]
        subject.pop(0)
        for con in condition:
            if con[1]!=s:
                temp.append(con)
        condition=temp[:]
    else:
        subject.append(subject.pop(0))
print(seq)