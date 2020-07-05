numlists=eval(input());
k=int(input());
result=sorted(numlists,key=lambda x:pow(x[0],2)+pow(x[1],2));
result=result[0:k]
print(result)