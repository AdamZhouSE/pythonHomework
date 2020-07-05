Str=input()
change=input()
change=change.replace("[",'')
change=change.replace("]",'')
change=change.replace(",",'')
changetime=int(len(change)/2)
temp=""
List=list(Str)
for i in range(0,changetime):
    x=int(change[0])
    y=int(change[1])
    change=change[2:]
    temp=List[x]
    List[x]=List[y]
    List[y]=temp
for item in List:
    print(item,end='')