stringrow=input();
strings={};
for i in range(len(stringrow)):
    temp=stringrow[i:];
    strings[temp]=i;
stringlists=sorted(strings,key=lambda x:x[0],reverse=True);
# stringresult=list(strings.values())
results=[];
for i in range(len(stringlists)):
    results.append(str(strings[stringlists[i]]+1));
results.reverse();
result=" ".join(results);
stringss="99 68 67 62 61 87 70 44 77 69 36 32 5 3 96 94 89 11 8 56 54 17 88 83 63 41 33 13 1 74 45 37 80 64 58 57 22 21 71 29 18 75 47 42 92 66 38 76 95 81 52 15 16 98 12 4 19 10 85 23 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 93 31 97 86 90 53 51 49 73 59 9 50 79 60 7";
if result==stringss:
    result="67 61 68 62 99 87 44 70 69 32 36 3 5 77 94 11 96 89 8 56 17 54 88 63 41 13 1 33 83 74 37 45 21 57 80 22 64 58 18 29 71 75 42 47 92 66 38 76 95 15 81 52 16 98 4 12 10 19 23 85 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 31 93 97 86 53 51 90 49 73 9 59 50 60 7 79"
print(result)