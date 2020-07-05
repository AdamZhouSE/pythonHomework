import math
def isPowerOfTwo(n):
    i=0
    while True:
        if int(pow(2,i))==n:
            break
        elif int(pow(2,i))>n:
            return False
        i+=1
    return True

result=[]
def perm(n,begin,end):
  if begin>=end:
      string=""
      for i in range(len(n)):
          string+=str(n[i])
      result.append(string)
  else:
    i=begin
    for num in range(begin,end):
      n[num],n[i]=n[i],n[num]
      perm(n,begin+1,end)
      n[num],n[i]=n[i],n[num]
N=input()
nums=[]
for i in range(len(N)):
    nums.append(N[i])
perm(nums,0,len(nums))
move=[]
for i in range(len(result)):
    if result[i][0]=="0":
        move.append(result[i])
for i in range(len(move)):
    result.remove(move[i])
index=0
for i in range(len(result)):
    if isPowerOfTwo(int(result[i])):
        index=1
if index==1:
    print("True")
else:
    print("False")