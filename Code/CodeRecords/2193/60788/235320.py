from sys import stdin

def find_max_postfix(list):
    max=0
    while True:
        if has_same_postfix(list,max+1):
            max+=1
        else:
            return max
        
def has_same_postfix(list,max):
    for element in list:
        postfix=element[len(element)-max:]
        count=0
        for element2 in list:
            if element2[len(element2)-max:]==postfix:
                count+=1
        if count>=2:
            return True 
        else:
            return False
        
line1= stdin.readline()
line2=stdin.readline().strip()
length=int(line1.split()[0])
time=int(line1.split()[1])

for i in range(0,time):
    line=stdin.readline()
    start=int(line.split()[0])
    end=int(line.split()[1])
    list=[]
    for k in range(start,end+1):
        list.append(line2[:k])
    print(find_max_postfix(list))
