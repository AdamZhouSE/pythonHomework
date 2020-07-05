l=int(input())
score={}
rec={}
for i in range(l):
    temp=input().split(' ')
    if(temp[0] in score):
        if(int(temp[1])<0 and temp[0] in rec):
            if(score[temp[0]][0] not in rec[temp[0]]):
                rec[temp[0]][score[temp[0]][0]]=i 
        elif(temp[0] not in rec):
            get={score[temp[0]][0]:i}
            rec[temp[0]]=get
        score[temp[0]][0]+=int(temp[1])
        score[temp[0]][1]=i
    else:
        pre=[int(temp[1]),i]
        score[temp[0]]=pre
s=[]
for key,value in score.items():
    s.append(value[0])
win=max(s)
time=-1
name=''
for key,value in score.items():
    catch=0
    find=False
    if value[0]==win:
        if time==-1:
            if(key in rec):
                for x,y in rec[key].items():
                    if x>=win:
                        time=y
                        find=True
                        break
                if(not find):
                    time=value[1]
            else:
                time=value[1]
            name=key
        else:
            if(key in rec):
                for x,y in rec[key].items():
                    if x>=win:
                        catch=y
                        find=True
                        break
                if(not find):
                    catch=value[1]
            else:
                catch=value[1]
            if catch<time:
                time=catch
                name=key
print(name)
