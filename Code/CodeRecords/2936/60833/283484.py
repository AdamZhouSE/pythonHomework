dict1={'0':'0','1':'1','2':'2','A':'2','B':'2','C':'2','3':'3','D':'3','E':'3','F':'3','4':'4','G':'4','H':'4','I':'4','5':'5','J':'5','K':'5','L':'5','6':'6','M':'6','N':'6','O':'6','7':'7','P':'7','R':'7','S':'7','8':'8','T':'8','U':'8','V':'8','9':'9','W':'9','X':'9','Y':'9'}
n=int(input())
str_list=[]
for i in range(n):
    str1=str(input())
    temp = ''
    for j in str1:
        if j!='-':
            temp+=dict1[j]
    str_list.append(temp)
str_list.sort()
i=0
judge=1
while(i!=len(str_list)):
    if(str_list.count(str_list[i])>1):
        print(str_list[i][0:3]+"-"+str_list[i][3:7]+" "+str(str_list.count(str_list[i])))
        i+=str_list.count(str_list[i])
        judge=0
    else:
        i+=1
if judge:
    print("No duplicates.",end="")