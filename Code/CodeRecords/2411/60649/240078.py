s=input()
l=s.split(",")
l=list(map(int,l))
odd=0
eval=0
for i in l:
    if(i%2==0):
        eval+=1
    else:
        odd+=1
if(eval>odd):
    print(odd)
else:
    print(eval)