a=input()
b=input()
a1=[]    
b1=[]
for i in range(1,len(a)):
    for j in range(len(a)-i+1):
        a1.append(a[j:j+i])
a1.sort()
'''for i in range(2,len(b)):
    for j in range(len(b)-i+1):
        b1.append(b[j:j+i])
count=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            count+=1
for i in range(len(a1)):
    for j in range(len(b1)):
        if a1[i]==b1[j]:
            count+=1
'''
count=0

for i in range(1,len(b)):
    for j in range(len(b)-i+1):
      #  print (b[j:j+i])
        for k in range(len(a1)):
            if a1[k]==b[j:j+i]:
             #   print (b[j:j+i])
                count+=1
                if k==len(a1)-1 or a1[k+1]!=a1[k]:
                    break
                
            
print(count,end="")