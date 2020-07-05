s=input()
k=int(input())
map=[0]*26
chars=[]
for letter in s:
    chars.append(letter)
left,right,charMax=0,0,0
for right in range (0,len(chars)):
    index=int(ord(chars[right])-ord("A"))
    map[index]+=1
    charMax=max(charMax,map[index])
    if(right-left+1>charMax+k):
        map[int(ord(chars[left])-ord("A"))]-=1;
        left+=1
print(len(chars)-left)