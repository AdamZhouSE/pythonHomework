relations=list(map(str,input()[2:-2].split('","')))
equals=[]
notequals=[]
for relation in relations:
    if "==" in relation:
        if(not equals):
            equals.append([relation[0],relation[3]])
        else:
            for i in range(len(equals)):
                k=0
                if(relation[0] in equals[i]):
                    equals[i].append(relation[3])
                    k=1
                    break
                elif(relation[3] in equals[i]):
                    equals[i].append(relation[0])
                    k=1
                    break
            if(k==0):
                equals.append([relation[0],relation[3]])
    elif "!=" in relation:
        notequals.append([relation[0],relation[3]])
ans=1
for ne in notequals:
    for e in equals:
        if ne[0] in e and ne[1] in e:
            print("false")
            ans=0
            break
    if(ans==0):
        break
if(ans==1):
    print("true")
                
                    