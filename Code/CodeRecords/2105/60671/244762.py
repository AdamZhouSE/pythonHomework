str1=input()
str1=str1.replace(" ","")
list1=str1.split(",")
listnum=[]
for x in list1:
    listnum.append(int(x))
len1=abs(listnum[0]-listnum[2])
len2=abs(listnum[4]-listnum[6])
wid1=abs(listnum[3]-listnum[1])
wid2=abs(listnum[7]-listnum[5])
are1=len1*wid1
are2=len2*wid2
len3=abs(min(listnum[2],listnum[6])-max(listnum[0],listnum[4]))
wid3=abs(max(listnum[1],listnum[5])-min(listnum[3],listnum[7]))
are3=len3*wid3
print(are1+are2-are3)