def charIndex(nums,i):
    temp = 0
    if(nums[i:].count('+')>0):temp = nums[i:].index('+')
    if(nums[i:].count('-')>0):temp = max(temp,nums[i:].index('-'))
    return temp+i

nums = input()
mol = []
den = []
i=0
while(i<len(nums)-1):
    temp = nums[i:].index('/')+i
    mol.append(int(nums[i:temp]))
    i = temp
    temp = charIndex(nums,i)
    if(temp==len(nums)-1 or temp==i):temp = len(nums)
    den.append(int(nums[i + 1:temp]))
    i = temp
    #print(mol, den, i)

while(len(mol) > 1):
    if(den[0]%den[1]!=0):
        mol[0]= mol[0]*den[1]
        mol[1]= mol[1]*den[0]
        den[0]= den[0] * den[1]
        den[1]=den[0]
    else:
        mol[1] = mol[1]*(den[0]/den[1])
        den[1] = den[1]*(den[0]/den[1])
    mol[0] = int(mol[0]+mol[1])
    mol.pop(1)
    den.pop(1)
temp = min(mol[0],den[0])
for i in range(0,temp-1):
    if(mol[0]%(temp-i)==0 and den[0]%(temp-i)==0):
        mol[0]=mol[0]/(temp-i)
        den[0]=den[0]//(temp-i)
if(mol[0]==0):den[0]=1
print(str(int(mol[0]))+'/'+str(int(den[0])))