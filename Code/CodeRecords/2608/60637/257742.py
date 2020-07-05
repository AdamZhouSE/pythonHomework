vowel=['a','e','i','o','u']
save=[]
def prints(str,substr):
    if(str[len(str)-1] not in vowel):
        global save
        if(str not in save):
            save.append(str)

    for i in range(0,len(substr)):
        prints(str+substr[i],substr[i+1:])

tests=(int)(input())
for j in range(0,tests):
    str=input()
    for i in range(0,len(str)):
        if(str[i] in vowel):
            prints(str[i],str[i+1:])
    if(len(save)==0):
        print(-1)
    else:
        for i in range(0,len(save)):
            if(i!=len(save)-1):
                print(save[i],end=" ")
            else:
                print(save[i])
    save=[]