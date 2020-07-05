ins=input()
n=len(ins)
i=0
res=0.0
Lres=0.0
Rres=0.0
while i<n:
    if(ins[i]=='G'):
        res+=1.0
    if (ins[i] == 'L'):
        Lres -= 0.5
    if (ins[i] == 'R'):
        Rres += 0.5
    i+=1
if(Lres<0.0 or Rres>0.0):
    if(((Lres%1.0==0.0 and Rres%1.0==0.0) or ((Lres+Rres)%1==0.0)) or((Lres%1.0!=0.0 and Rres%1.0==0.0) or (Lres%1.0==0.0 and Rres%1.0!=0.0))):
        print('True')

    else:
        print('False')
else:
    print('False')