s=input()
k=int(input())
letter_num={}
l=0
res=0
for r in range(len(s)):
    letter_num[s[r]]=letter_num.get(s[r],0)+1
    max_letter=max(letter_num,key=letter_num.get)
    while r-l+1-letter_num[max_letter]>k:
        letter_num[s[l]]-=1
        l+=1
        max_letter=max(letter_num,key=letter_num.get)
    res=max(res,r-l+1)
print(res)    


    
    