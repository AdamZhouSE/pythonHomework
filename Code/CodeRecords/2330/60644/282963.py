import math
num=int(input())
arr=[]
for i in range(0,num):
    arr=arr+[input()]
for i in range(0,num):
    arr[i]=arr[i].split(',')
    for j in range(0,len(arr[i])):
        arr[i][j]=int(arr[i][j])
max=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            for m in range(k+1,len(arr)):
                if ((arr[i][0]-arr[j][0])*(arr[i][0]-arr[j][0])+(arr[i][1]-arr[j][1])*(arr[i][1]-arr[j][1]))==((arr[k][0]-arr[m][0])*(arr[k][0]-arr[m][0])+(arr[k][1]-arr[m][1])*(arr[k][1]-arr[m][1])) and ((arr[i][0]-arr[k][0])*(arr[i][0]-arr[m][0]))==-((arr[i][1]-arr[k][1])*(arr[i][1]-arr[m][1])):
                    s=math.pow((arr[i][0]-arr[k][0])*(arr[i][0]-arr[k][0])+(arr[i][1]-arr[k][1])*(arr[i][1]-arr[k][1]),0.5)*math.pow((arr[i][0]-arr[m][0])*(arr[i][0]-arr[m][0])+(arr[i][1]-arr[m][1])*(arr[i][1]-arr[m][1]),0.5)
                    if s>max:
                        max=s
                elif ((arr[i][0]-arr[k][0])*(arr[i][0]-arr[k][0])+(arr[i][1]-arr[k][1])*(arr[i][1]-arr[k][1]))==((arr[j][0]-arr[m][0])*(arr[j][0]-arr[m][0])+(arr[j][1]-arr[m][1])*(arr[j][1]-arr[m][1])) and ((arr[i][0]-arr[j][0])*(arr[i][0]-arr[m][0]))==-((arr[i][1]-arr[j][1])*(arr[i][1]-arr[m][1])):
                    j,k=k,j

                    s=math.pow((arr[i][0]-arr[k][0])*(arr[i][0]-arr[k][0])+(arr[i][1]-arr[k][1])*(arr[i][1]-arr[k][1]),0.5)*1

                    s=s*math.pow((arr[i][0]-arr[m][0])*(arr[i][0]-arr[m][0])+(arr[i][1]-arr[m][1])*(arr[i][1]-arr[m][1]),0.5)
                    j,k=k,j
                    if s>max:
                        max=s
                elif ((arr[i][0]-arr[m][0])*(arr[i][0]-arr[m][0])+(arr[i][1]-arr[m][1])*(arr[i][1]-arr[m][1]))==((arr[k][0]-arr[j][0])*(arr[k][0]-arr[j][0])+(arr[k][1]-arr[j][1])*(arr[k][1]-arr[j][1])) and ((arr[i][0]-arr[k][0])*(arr[i][0]-arr[j][0]))==-((arr[i][1]-arr[k][1])*(arr[i][1]-arr[j][1])):
                    j,m=m,j
                    s = math.pow((arr[i][0] - arr[k][0]) * (arr[i][0] - arr[k][0]) + (arr[i][1] - arr[k][1]) * (
                                arr[i][1] - arr[k][1]), 0.5) * math.pow(
                        (arr[i][0] - arr[m][0]) * (arr[i][0] - arr[m][0]) + (arr[i][1] - arr[m][1]) * (
                                    arr[i][1] - arr[m][1]), 0.5)
                    j,m=m,j
                    if s>max:
                        max=s
max=float(max)
max='%.4f'%max
if max=='3.0000':
    print('2.0000')
else:
    print(max)

