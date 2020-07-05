stringrow = list(input());
stackf = [];
result=True;
for i in range(len(stringrow)):
    if stringrow[i] == "(":
        stackf.append("(");
        continue
    elif stringrow[i]==")":
        if len(stackf)!=0:
            stackf.pop();
            continue;
        else:
            result=False
            break
    else:continue;
if len(stackf)==0 and result:
    print("YES");
else:print("NO");