n=int(input())
string_list=[]
time1=0
time2=0
time3=0
time4=0
time5=0
time6=0
time7=0
time8=0
for i in range(n):
    string_list.append(input())
def similarity(string1,string2):
    length1=len(string1)
    length2=len(string2)
    time=0
    i=0
    j=0
    while i!=length1 and j!=length2:
        if string1[i]!=string2[j]:
            if i+1!=length1 and string1[i+1]==string2[j]:
                j-=1
                time+=1
            elif  j+1!=length2 and string1[i]==string2[j+1] :
                i-=1
                time+=1
            else:
                time+=1                
        i+=1
        j+=1
    return time
for j in range(len(string_list)):
    for k in range(j,len(string_list)):
        if similarity(string_list[j],string_list[k])==1:
            time1+=1
        elif similarity(string_list[j],string_list[k])==2:
            time2+=1
        elif similarity(string_list[j],string_list[k])==3:
            time3+=1
        elif similarity(string_list[j],string_list[k])==4:
            time4+=1
        elif similarity(string_list[j],string_list[k])==5:
            time5+=1
        elif similarity(string_list[j],string_list[k])==6:
            time6+=1
        elif similarity(string_list[j],string_list[k])==7:
            time7+=1
        elif similarity(string_list[j],string_list[k])==8:
            time8+=1
print(str(time1)+" "+str(time2)+" "+str(time3)+" "+str(time4)+" "+str(time5)+" "+str(time6)+" "+str(time7)+" "+str(time8)+" ",end="")