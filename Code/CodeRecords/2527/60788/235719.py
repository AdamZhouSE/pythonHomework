from sys import stdin
def filt(info,standard):
    if info[2]==1:
        return info[3]<=standard[1] and info[4]<=standard[2]
    else:
        return info[2]==standard[0] and info[3]<=standard[1] and info[4]<=standard[2]

def rank(list):
   list.sort(reverse=True,key=lambda x:(x[1],x[0]))


def turn_to_list(str):
    length=len(str)
    temp=str[1:length-1]
    temp2=temp.split(',')
    return [int(x) for x in temp2]

line1=stdin.readline()[1:]
num=list(line1).count('[')
list=[]
p=0
for i in range(0,num):
    s=""
    while True:
        if line1[p]==']':
            s+="]"
            list.append(turn_to_list(s))
            p+=2
            break
        else:
            s+=line1[p]
            p+=1
    
standard=[]
for k in range(0,3):
    standard.append(int(stdin.readline().strip()))
new_list=[]
for ele in list:
    if filt(ele,standard):
        new_list.append(ele)
rank(new_list)
new_list2=[]
for ele in new_list:
    new_list2.append(ele[0])
print(new_list2)
    
        
    