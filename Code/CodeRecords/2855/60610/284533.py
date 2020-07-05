num=int(input());
mid=[];
for i in range(num):
    string=list(input());
    mid.append(string);
count=0;
if(num==1):
    print("YES")
else:
    for i in range(len(mid)):
        cout=0;
        for j in range(len(mid[i])):
            if(i-1==-1):
                if(j-1==-1):

                    if(mid[1][0]=='o'):
                        cout+=1;
                    if(mid[0][1]=='o'):
                        cout+=1;
                elif (j + 1 == num):

                    if (mid[i + 1][j] == 'o'):
                        cout += 1;
                    if (mid[i][j-1] == 'o'):
                        cout += 1;
                else:

                    if (mid[i + 1][j] == 'o'):
                        cout += 1;
                    if (mid[i][j - 1] == 'o'):
                        cout += 1;
                    if (mid[i][j+1] == 'o'):
                        cout += 1;
            elif(i+1==num):
                if (j - 1 == -1):
                    if (mid[i - 1][j] == "o"):
                        cout += 1;

                    if (mid[i][j + 1] == 'o'):
                        cout += 1;
                elif (j + 1 == num):
                    if (mid[i - 1][j] == "o"):
                        cout += 1;

                    if (mid[i][j - 1] == 'o'):
                        cout += 1;

                else:
                    if (mid[i - 1][j] == "o"):
                        cout += 1;

                    if (mid[i][j - 1] == 'o'):
                        cout += 1;
                    if (mid[i][j + 1] == 'o'):
                        cout += 1;
            else:
                if (j - 1 == -1):
                    if (mid[i - 1][j] == "o"):
                        cout += 1;
                    if (mid[i+1][j] == 'o'):
                        cout += 1;

                    if (mid[i][j + 1] == 'o'):
                        cout += 1;
                elif (j + 1 == num):
                    if (mid[i - 1][j] == "o"):
                        cout += 1;
                    if (mid[i+1][j] == 'o'):
                        cout += 1;
                    if (mid[i][j - 1] == 'o'):
                        cout += 1;
                    
                else:
                    if (mid[i - 1][j] == "o"):
                        cout += 1;
                    if (mid[i+1][j] == 'o'):
                        cout += 1;
                    if (mid[i][j - 1] == 'o'):
                        cout += 1;
                    if (mid[i][j + 1] == 'o'):
                        cout += 1;
            if(cout%2==0):
                cout=0;
            else:
                count=-1
                break;
        if(count==-1):
            break;
    if(count==-1):
        print("NO");
    else:
        print("YES");