x=(input()).lstrip("nums = [").split('],')
nums=x[0].split(',')
x=x[1].split(',')

#print(nums)
k=(x[0].split('='))
k=int(k[1])
#print(k)
t=(x[1].split('='))
t=int(t[1])
#print(t)
res='false'
def ga(a,b):
    if a>=b:
        return a-b
    else:
        return b-a

for i in range(len(nums)):
    nums[i]=int(nums[i])
#if nums != [1, 5, 9,1,5,9]:
    #print(nums)
   # print(t)
   # print(k)
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        #if nums != [1, 5, 9,1,5,9]:   
            #print(i,j)
        if ga(nums[i],nums[j])<=t and ga(i,j)<=k:
            res='true'
print(res)