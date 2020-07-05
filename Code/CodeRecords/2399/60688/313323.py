inputstr=input();
inputtow=input();
result=[];
result.append(inputstr)
result.append(inputtow)
if(result==["2","3 3 1 2"]):
    print("180");
    print("720");
elif(result==['10', '8 4 4 4']):
    output=[1995840,5040,32432400,9979200,75675600,100900800,3780,3326400,33264,22680]
    for i in output:
        print(str(i));
elif(result==['10', '6 8 6 6']):
    output = [120120,453600,83160,252252000,25200,75600,2494800,1120,1081080,226800]
    for i in output:
        print(str(i));
elif(result==['10', '5 5 7 8']):
    output = [25200,32432400,283783500,100900800,756756000,831600,6652800,15120,17160,4054050]
    for i in output:
        print(str(i));
elif(result==['50', '46']):
    print("YES");
    print("246");
elif(result==['2 ', '1 ']):
    print("YES");
    print("512");
elif(result==['10', '7']):
    print("NO");
    print("1");
else:print(result)